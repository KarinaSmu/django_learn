from django.shortcuts import render
from django.http import HttpResponse
import logging

# Настройка логирования
logger = logging.getLogger(__name__)

def index(request):
    logger.info('Посещение главной страницы')
    return render(request, "myapp/index.html")

def about(request):
    logger.info('Посещение страницы о себе')
    return render(request, "myapp/about.html")

# Create your views here.
