from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


class Command(BaseCommand):
    help = 'Create superuser for Railway deployment'

    def handle(self, *args, **options):
        try:
            # Check if admin user already exists
            if User.objects.filter(username='admin').exists():
                self.stdout.write('Admin user already exists!')
                return
            
            # Create new superuser
            User.objects.create_superuser(
                username='admin',
                email='admin@asliddin.edu',
                password='admin123'
            )
            
            self.stdout.write(
                self.style.SUCCESS('Superuser created successfully!')
            )
            self.stdout.write('Username: admin')
            self.stdout.write('Password: admin123')
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating superuser: {e}')
            )
