from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create superuser for Railway deployment'

    def handle(self, *args, **options):
        # Delete existing admin user if exists
        User.objects.filter(username='admin').delete()
        
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
