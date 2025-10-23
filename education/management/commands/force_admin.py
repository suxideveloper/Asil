from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


class Command(BaseCommand):
    help = 'Force create admin user with environment variables'

    def handle(self, *args, **options):
        try:
            # Get credentials from environment variables
            username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
            email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@asliddin.edu')
            password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')
            
            # Delete existing admin user
            User.objects.filter(username=username).delete()
            
            # Create new admin user
            admin_user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            
            self.stdout.write(
                self.style.SUCCESS(f'Admin user {username} created successfully!')
            )
            self.stdout.write(f'Username: {username}')
            self.stdout.write(f'Password: {password}')
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating admin user: {e}')
            )
