from django.urls import path
from shopapp.views import client_order, clients, orders, index

urlpatterns = [
    path('orders/<int:id>/<str:period>/', client_order, name='client_order'),
    path('orders/', orders, name='orders'),
    path('clients/', clients, name='clients'),
    path('', index, name='index'),
]