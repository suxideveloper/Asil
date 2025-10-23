from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Simple admin user creation'

    def handle(self, *args, **options):
        # Delete all users
        User.objects.all().delete()
        
        # Create simple admin
        User.objects.create_superuser('admin', 'admin@asliddin.edu', 'password123')
        
        self.stdout.write('Admin created: admin / password123')
