from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction
import os


class Command(BaseCommand):
    help = 'Create admin user specifically for Railway deployment'

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                # Delete all existing users to start fresh
                User.objects.all().delete()
                
                # Create admin user with hardcoded credentials
                admin_user = User.objects.create_superuser(
                    username='admin',
                    email='admin@asliddin.edu',
                    password='admin123'
                )
                
                # Also create a test user
                test_user = User.objects.create_user(
                    username='test',
                    email='test@asliddin.edu',
                    password='test123'
                )
                
                self.stdout.write(
                    self.style.SUCCESS('Railway admin user created successfully!')
                )
                self.stdout.write('Username: admin')
                self.stdout.write('Password: admin123')
                self.stdout.write('Email: admin@asliddin.edu')
                self.stdout.write('')
                self.stdout.write('Test user also created:')
                self.stdout.write('Username: test')
                self.stdout.write('Password: test123')
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating Railway admin: {e}')
            )
