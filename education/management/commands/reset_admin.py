from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Reset admin user password and permissions'

    def handle(self, *args, **options):
        try:
            # Delete existing admin user if exists
            User.objects.filter(username='admin').delete()
            
            # Create new admin user
            admin_user = User.objects.create_superuser(
                username='admin',
                email='admin@asliddin.edu',
                password='admin123'
            )
            
            self.stdout.write(
                self.style.SUCCESS('Admin user reset successfully!')
            )
            self.stdout.write('Username: admin')
            self.stdout.write('Password: admin123')
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error resetting admin user: {e}')
            )
