from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction


class Command(BaseCommand):
    help = 'Fix admin user - delete all users and create fresh admin'

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                # Delete all existing users
                User.objects.all().delete()
                
                # Create fresh admin user
                admin_user = User.objects.create_superuser(
                    username='admin',
                    email='admin@asliddin.edu',
                    password='admin123'
                )
                
                # Create additional test user
                test_user = User.objects.create_user(
                    username='test',
                    email='test@asliddin.edu',
                    password='test123'
                )
                
                self.stdout.write(
                    self.style.SUCCESS('Database reset successfully!')
                )
                self.stdout.write('Admin user created:')
                self.stdout.write('Username: admin')
                self.stdout.write('Password: admin123')
                self.stdout.write('')
                self.stdout.write('Test user created:')
                self.stdout.write('Username: test')
                self.stdout.write('Password: test123')
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error fixing admin: {e}')
            )
