from django.core.management.base import BaseCommand
from shopapp.models import Client


class Command(BaseCommand):
    help = "Get necessary client"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int,help="Client ID")

    def handle(self, *args, **kwargs):
        pk = kwargs["pk"]
        client = Client.objects.filter(pk=pk).first()
        self.stdout.write(f'{client}')
