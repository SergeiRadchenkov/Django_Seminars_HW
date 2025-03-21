from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def home(request):
    html = """
    <html>
        <head><title>Главная</title></head>
        <body>
            <h1>Добро пожаловать на мой Django-сайт!</h1>
            <p>Этот сайт создан для обучения работе с Django.</p>
        </body>
    </html>
    """
    logger.info("Главная страница была посещена.")
    return HttpResponse(html)


def about(request):
    html = """
    <html>
        <head><title>О себе</title></head>
        <body>
            <h1>Обо мне</h1>
            <p>Меня зовут Сергей. Я изучаю Django и создаю свои проекты.</p>
        </body>
    </html>
    """
    logger.info("Страница 'О себе' была посещена.")
    return HttpResponse(html)
