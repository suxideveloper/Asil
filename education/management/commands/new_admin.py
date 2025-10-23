from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction
import os


class Command(BaseCommand):
    help = 'Create admin user with new password'

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                # Delete all existing users
                User.objects.all().delete()
                
                # Create admin user with new password
                admin_user = User.objects.create_superuser(
                    username='admin',
                    email='admin@asliddin.edu',
                    password='password123'
                )
                
                # Also create a simple user
                simple_user = User.objects.create_user(
                    username='user',
                    email='user@asliddin.edu',
                    password='user123'
                )
                
                self.stdout.write(
                    self.style.SUCCESS('New admin user created successfully!')
                )
                self.stdout.write('Username: admin')
                self.stdout.write('Password: password123')
                self.stdout.write('Email: admin@asliddin.edu')
                self.stdout.write('')
                self.stdout.write('Simple user also created:')
                self.stdout.write('Username: user')
                self.stdout.write('Password: user123')
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating admin user: {e}')
            )
