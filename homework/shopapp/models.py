from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Клиент {self.name} ({self.email})"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Товар {self.name} (Цена: {self.price})"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_placed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заказ №{self.id} от {self.date_placed.strftime('%Y-%m-%d')} на сумму {self.total_amount}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Заказ №{self.order.id} - {self.product.name} (Количество: {self.quantity})"


# # CRUD функции для модели Клиент
# def create_client(name, email, phone, address):
#     client = Client(name=name, email=email, phone=phone, address=address)
#     client.save()
#     return client
#
#
# def get_client(client_id):
#     return Client.objects.get(id=client_id)
#
#
# def update_client(client_id, **kwargs):
#     Client.objects.filter(id=client_id).update(**kwargs)
#
#
# def delete_client(client_id):
#     client = Client.objects.get(id=client_id)
#     client.delete()
#
#
# # CRUD функции для модели Товар
# def create_product(name, description, price, quantity):
#     product = Product(name=name, description=description, price=price, quantity=quantity)
#     product.save()
#     return product
#
#
# def get_product(product_id):
#     return Product.objects.get(id=product_id)
#
#
# def update_product(product_id, **kwargs):
#     Product.objects.filter(id=product_id).update(**kwargs)
#
#
# def delete_product(product_id):
#     product = Product.objects.get(id=product_id)
#     product.delete()
#
#
# # CRUD функции для модели Заказ
# def create_order(client, total_amount):
#     order = Order(client=client, total_amount=total_amount)
#     order.save()
#     return order
#
#
# def get_order(order_id):
#     return Order.objects.get(id=order_id)
#
#
# def update_order(order_id, **kwargs):
#     Order.objects.filter(id=order_id).update(**kwargs)
#
#
# def delete_order(order_id):
#     order = Order.objects.get(id=order_id)
#     order.delete()
#
#
# # Для добавления товаров в заказ используйте функцию ниже
# def add_product_to_order(order, product, quantity):
#     order_item = OrderItem(order=order, product=product, quantity=quantity)
#     order_item.save()
