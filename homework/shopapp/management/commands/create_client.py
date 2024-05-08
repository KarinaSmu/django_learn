from django.core.management.base import BaseCommand
from shopapp.models import Client


class Command(BaseCommand):
    help = "Creating new client"

    def handle(self, *args, **kwargs):
        # client = Client(name='client1', email='email1', phone='800200', address='address1')
        # client = Client(name='client2', email='email2', phone='800200', address='address2')
        client = Client(name='client3', email='email3', phone='800200', address='address3')
        client.save()
        self.stdout.write(f'{client}')
