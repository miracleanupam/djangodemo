from django.core.management.base import BaseCommand
from user.models import User


class Command(BaseCommand):
    help = 'Creates a normal user for testing purposes'

    def handle(self, *args, **options):
        if User.objects.filter(username='testuser').count() == 0:
            new_admin_user = User.objects.create(
                username='testuser',
                email='testuser@tet.com'
            )
            new_admin_user.set_password('testtest')
            new_admin_user.save()
