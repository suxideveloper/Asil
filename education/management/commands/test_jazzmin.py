from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Test Jazzmin configuration'

    def handle(self, *args, **options):
        self.stdout.write('Testing Jazzmin configuration...')
        
        # Check if Jazzmin is in INSTALLED_APPS
        if 'jazzmin' in settings.INSTALLED_APPS:
            self.stdout.write(self.style.SUCCESS('✓ Jazzmin is in INSTALLED_APPS'))
        else:
            self.stdout.write(self.style.ERROR('✗ Jazzmin is NOT in INSTALLED_APPS'))
        
        # Check Jazzmin settings
        if hasattr(settings, 'JAZZMIN_SETTINGS'):
            self.stdout.write(self.style.SUCCESS('✓ JAZZMIN_SETTINGS found'))
            self.stdout.write(f'  Site title: {settings.JAZZMIN_SETTINGS.get("site_title", "Not set")}')
        else:
            self.stdout.write(self.style.ERROR('✗ JAZZMIN_SETTINGS not found'))
        
        # Check if admin is before jazzmin
        admin_index = settings.INSTALLED_APPS.index('django.contrib.admin') if 'django.contrib.admin' in settings.INSTALLED_APPS else -1
        jazzmin_index = settings.INSTALLED_APPS.index('jazzmin') if 'jazzmin' in settings.INSTALLED_APPS else -1
        
        if jazzmin_index < admin_index:
            self.stdout.write(self.style.SUCCESS('✓ Jazzmin is before django.contrib.admin'))
        else:
            self.stdout.write(self.style.ERROR('✗ Jazzmin should be before django.contrib.admin'))
        
        self.stdout.write('Jazzmin test completed!')
