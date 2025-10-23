from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction
import os


class Command(BaseCommand):
    help = 'Ensure admin user exists with correct credentials'

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                # Get credentials from environment or use defaults
                username = os.environ.get('ADMIN_USERNAME', 'admin')
                email = os.environ.get('ADMIN_EMAIL', 'admin@asliddin.edu')
                password = os.environ.get('ADMIN_PASSWORD', 'admin123')
                
                # Delete existing admin user
                User.objects.filter(username=username).delete()
                
                # Create fresh admin user
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
                self.stdout.write(f'Email: {email}')
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating admin user: {e}')
            )
