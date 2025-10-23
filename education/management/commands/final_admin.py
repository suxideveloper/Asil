from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction


class Command(BaseCommand):
    help = 'Final admin user creation for Railway'

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                # Delete all existing users
                User.objects.all().delete()
                
                # Create admin user
                admin = User.objects.create_superuser(
                    username='admin',
                    email='admin@asliddin.edu',
                    password='password123'
                )
                
                # Create test user
                test_user = User.objects.create_user(
                    username='test',
                    email='test@asliddin.edu',
                    password='test123'
                )
                
                self.stdout.write('✅ Admin user created successfully!')
                self.stdout.write('Username: admin')
                self.stdout.write('Password: password123')
                self.stdout.write('')
                self.stdout.write('✅ Test user also created:')
                self.stdout.write('Username: test')
                self.stdout.write('Password: test123')
                
        except Exception as e:
            self.stdout.write(f'❌ Error: {e}')
