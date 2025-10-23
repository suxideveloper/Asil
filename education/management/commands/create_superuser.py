from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


class Command(BaseCommand):
    help = 'Create superuser for Railway deployment'

    def handle(self, *args, **options):
        try:
            # Get or create admin user
            admin_user, created = User.objects.get_or_create(
                username='admin',
                defaults={
                    'email': 'admin@asliddin.edu',
                    'is_staff': True,
                    'is_superuser': True
                }
            )
            
            # Always update password to ensure it's correct
            admin_user.set_password('admin123')
            admin_user.is_staff = True
            admin_user.is_superuser = True
            admin_user.is_active = True
            admin_user.save()
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS('Superuser created successfully!')
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS('Admin user password updated!')
                )
            
            self.stdout.write('Username: admin')
            self.stdout.write('Password: admin123')
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating/updating superuser: {e}')
            )
