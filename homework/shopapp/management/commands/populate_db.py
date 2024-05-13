from faker import Faker
import random
from django.core.management.base import BaseCommand
from shopapp.models import Client, Product, Order, OrderItem

class Command(BaseCommand):
    help = "Populating db with fake data"

    def handle(self, *args, **kwargs):
        self.create_clients(10)
        self.create_products(50)
        self.create_orders(20)
        if 'pk' in kwargs and 'name' in kwargs:
            self.update_client_name(kwargs['pk'], kwargs['name'])

    def create_clients(self, n):
        fake = Faker()
        for _ in range(n):
            Client.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                address=fake.address()
            )

    def create_products(self, n):
        fake = Faker()
        for _ in range(n):
            Product.objects.create(
                name=fake.word().capitalize(),
                description=fake.text(max_nb_chars=200),
                price=round(random.uniform(10.99, 999.99), 2),
                quantity=random.randint(1, 100)
            )

    def create_orders(self, n):
        clients = list(Client.objects.all())
        products = list(Product.objects.all())
        for _ in range(n):
            client = random.choice(clients)
            order = Order.objects.create(client=client, total_amount=0)
            for _ in range(random.randint(1, 5)):
                product = random.choice(products)
                quantity = random.randint(1, 10)
                OrderItem.objects.create(order=order, product=product, quantity=quantity)
                order.total_amount += product.price * quantity
            order.save()

    def update_client_name(self, pk, name):
        try:
            client = Client.objects.get(pk=pk)
            client.name = name
            client.save()
        except Client.DoesNotExist:
            print(f"Client with pk={pk} does not exist.")
