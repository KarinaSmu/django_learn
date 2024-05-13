from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Order, Product, Client


def client_order(request, id, period):
    if period == 'week':
        time_period = timezone.now() - timedelta(days=7)
    elif period == 'month':
        time_period = timezone.now() - timedelta(days=30)
    elif period == 'year':
        time_period = timezone.now() - timedelta(days=365)
    else:
        return JsonResponse({'error': 'Неверный период времени'},
                            json_dumps_params={'ensure_ascii': False},
                            status=400)

    orders = Order.objects.filter(client_id=id, date_placed__gte=time_period)
    products_ordered = Product.objects.filter(orderitem__order__in=orders).distinct()

    products_ordered = products_ordered.order_by('-date_added')

    products_list = [
        {'name': product.name, 'date_added': product.date_added}
        for product in products_ordered
    ]

    return JsonResponse({'products_ordered': products_list},
                        json_dumps_params={'ensure_ascii': False})


def clients(request):
    clients = Client.objects.all()
    return render(request, 'shopapp/clients.html', {'clients': clients})


def index(request):
    return render(request, "shopapp/index.html")


def orders(request):
    return HttpResponse("Здесь будет список заказов")
