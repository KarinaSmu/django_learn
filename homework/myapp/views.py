from django.shortcuts import render
from django.http import HttpResponse
import logging

# Настройка логирования
logger = logging.getLogger(__name__)

def index(request):
    logger.info('Посещение главной страницы')
    html = """
    <h1>Добро пожаловать на мой первый сайт на Django!</h1>
    <p>Это главная страница моего сайта. Здесь вы найдете информацию о проекте.</p>
    """
    return HttpResponse(html)

def about(request):
    logger.info('Посещение страницы о себе')
    html = """
    <h1>Обо мне</h1>
    <p>Привет! Я начинающий разработчик Django и это мой первый сайт.</p>
    <p>Здесь я буду делиться своими проектами и идеями.</p>
    """
    return HttpResponse(html)

# Create your views here.
