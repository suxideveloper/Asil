from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction
import os


class Command(BaseCommand):
    help = 'Force create admin user for Railway with multiple attempts'

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                # Delete all existing users
                User.objects.all().delete()
                
                # Create admin user with multiple attempts
                admin_user = User.objects.create_superuser(
                    username='admin',
                    email='admin@asliddin.edu',
                    password='admin123'
                )
                
                # Verify the user was created
                if admin_user:
                    self.stdout.write(
                        self.style.SUCCESS('Admin user created successfully!')
                    )
                    self.stdout.write('Username: admin')
                    self.stdout.write('Password: admin123')
                    self.stdout.write('Email: admin@asliddin.edu')
                    
                    # Test login
                    from django.contrib.auth import authenticate
                    user = authenticate(username='admin', password='admin123')
                    if user:
                        self.stdout.write('✅ Login test successful!')
                    else:
                        self.stdout.write('❌ Login test failed!')
                else:
                    self.stdout.write('❌ Failed to create admin user!')
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating admin user: {e}')
            )
