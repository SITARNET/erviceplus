# 1. Django

# Виртуальное окружение (venv) -> Python 3..3 + Django 3.1.4 (на Windows)

# localhost - 127.0.0.1

# python -V -> Python 3.9.13
# pip list
# cd C:/Users/SITARNET/python/serviceplus
# python -m venv venv - устанавливаем venv окружение под названием venv
# .\venv\Scripts\activate - запуск вертуального окружения
# python.exe -m pip install --upgrade pip - обновление pip
# deactivate - выйти из вертуального окружения
# открываем проэкт в PyCharm -> (venv) PS C:\Users\SITARNET\Documents\Python\serviceplus>
# pip install django - устанавливаем движок
# pip list -> ...
# django-admin - все комманды django
# django-admin startproject <имя сайта>
# django-admin startproject coolsite
# cd .\coolsite
# python manage.py runserver - запуск сервера
# http://127.0.0.1:8000
# CTRL+C - остановка сервера
# python manage.py runserver 40000 - меняем порт
# http://127.0.0.1:4000
# python manage.py runserver 192.168.1.1:4000 - меняем ip


# 2. Модель MTV. Маршрутизация. Функции представления

# MTV - models, templates, views
# Создаём приложение (пакет). Оно должно быть максимально независимым от других приложений
# python manage.py startapp service

# service -> admin.py -> админпанель сайта
# service -> apps.py -> для конфигурации приложения
# service -> models.py -> для хранения ORM моделей
# service -> tests.py -> тестирующие процедуры
# service -> views.py ->для хранения представления

# serviceplus -> settings.py -> INSTALLED_APPS -> 'service.apps.ServiceConfig' - регистрация пакета
# service -> views.py -> определяем предствление страницы (function или class)
# serviceplus -> urls.py -> path('service/', index) -> импортируем маршрут (связываем функцию index с url)
# serviceplus -> Mark Directory as -> Sources root - для корректного импортирования
# service -> urls.py - создаём свои маршруты в пакете (если будем переносить пакет на другой сайт)

# 3. Маршрутизация, обработка исключений запросов, перенаправления

# path('cats/<int:catsid>/', categories)
# str - любая не пустая строка, исключая символ /
# int - любое положительное, целое число включая 0
# slug - слаг, то есть, латиница ASCII таблицы, символы дефиса и подчёркивания
# uuid - цыфры, малые латинские ASCII, дефис
# path - любая не пустая строка, включая символ /
# re_path() - для использования регулярных выражений

# Обработка GET и POST запросов
# http://127.0.0.1:8000/?name=Gagarina&cat=music - GET запрос
# request.GET (POST)

# Обработка искючений при запросах к серверу
# serviceplus -> settings.py -> DEBUG = False - режим откладки отключён
# serviceplus -> settings.py -> ALLOWED_HOSTS = ['127.0.0.1']

# handler404 = pageNotFound -> serviceplus/urls.py
# serviceplus/view.py -> pageNotFound(request, exception)

# Обработка исключений при запросах к серыеру
# hundler500 - ошибка сервера
# hundler403 - доступ запрещён
# hundler400 - невозможно обработать запрос

# Создание 301 и 302 редиректов
# 301 - страница перемещена на другой постоянный URL-адрес
# 302 - страница перемещена на другой временный URL-адрес

# import django.shortcuts
# django.shortcuts.redirect

# return redirect('/', permanent=True)
# без параметра permanent -> 302
# c параметром permanent=True -> 301

# name='home' - используем имя для редиректа (serviceplus/urls.py)

# 4. Определение моделей. Миграции: создание и выполнение

# SQLite, MySQL, PortageSQL, Oracle...
# WSGI-приложение -> API интерфейс -> Django ORM -> Драйвер ORN -> SQLite....
# ORM (Object-Relation Mapping) - объектно-реляционное отображение
# sudo apt update
# sudo apt-cache search sqlite
# sudo apt install sqlite3
# sudo apt update
# sudo apt install sqlitebrowser

# serviceplus -> service -> models.py
# id: integer, primary key
# title: Varchar
# content: Text
# photo: Image
# time_create: DataTime
# Time_update: DataTime
# is_published: Boolean

# djbook.ru/rel3.0/ref/models/fields.html
# Чтобы Django могло сохранять фото, надо настроить две константы: FileField -> MEDIA_ROOT, MEDIA_URL
# serviceplus -> settings.py -> MEDIA_ROOT = os.path.join(BASE_DIR, 'media') -> import os
# MEDIA_URL = '/media/'

# Это настраиваеться только в откладочном режиме (не на реальном сервере) -> DEBUG = True
# serviceplus -> urls.py
# from django.conf.urls.static import static
# from serviceplus import settings
# if settings.DEBUG:
#       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Добавляем файлы миграций в папку "migration" -> чтобы добавить структуру таблиц
# ../serviceplus$ python manage.py makemigrations
# python -m pip install Pillow -> пакет для работы с фото
# service/migrations/0001_initial.py
# python manage.py sqlmigrate service 0001 -> посмотреть SQL-запрос для модели women под номером 0001
# python manage.py migrate -> запускаем миграцию (sql-запрос)

# 5. Django

# CRUD - Create, Read, Update, Delete
# ORM фркймворка Django

# python manage.py shell -> консоль фрймворка
# >>> from service.models import Service
# >>> Service(title='Ремонт ноутбуков', content='Ми делаем комплекс. Чистка, замена термопасты, настройка Windows')
# >>> w1 = _ - ссылка на объект Service
# >>> w1.save() - запись в таблицу
# >>> w1.id -> 1
# >>> w1.title -> Ремонт ноутбуков
# >>> w1.pk (=w1.id) -> 1
# >>> from django.db import connection
# >>> connection.queries - посмотреть SQL-запросы
# >>> w3 = Service()
# >>> w3.title = 'Ремонт системного блока'
# >>> w3.content = 'Полный комплекс работ по ремонту системного блока'
# >>> w3.save()

# Или используем другой метод
# >>> Service.objects
# >>> w4 = Service.objects.create(title='Заправка картриджей', content='Заправка или регенирация лазерных картриджей') - записываеться сразу в базу
# >>> w4
# >>> w4.title
# >>> w4.pk

# Можно без присвоения переменной
# >>> Service.objects.create(title='Кира Найтли', content='Биография Киры Найтли')
# >>> Service.objacts.all() - все текущие записи
# models.py -> def __str__(self): return self.title в классе Women
# >>> exit() - выходим из оболочки Django (перезапускаем)
# >>> python manage.py shell
# >>> from service.models import Service
# >>> Service.objects.all() -> <QuerySet [<Service: Анджелина Джоли>, <Service: Энн.... -> ограничение на 21 запись!
# >>> w = _ - присваеваем список
# >>> w[0] -> <Service: Анджелина Джоли>
# >>> w[0].title -> 'Анджелина Джоли'
# >>> len(w) -> 5
# >>> for wi in w: print(wi.title) -> Анджелина Джоли, Энн Хэтэуэй, Джулия Робертс, Ума Турман, Кира Найтли

# >>> Service.objects.filter(title='Энн Хэтэуэй') - выбока с помощью фильтра
# >>> Service.objects.filter(pk=2) -> <QuerySet [<Service: Энн Хэтэуэй>]>
# >>> Service.objects.filter() => <имя_атрибута>__gte - сравнение больше или равно (>=)
# >>> Service.objects.filter() => <имя_атрибута>__lte - сравнение меньше или равно (<=)
# >>> Service.objects.filter(pk__gte=2) => <QuerySet [<Service: Энн Хэтэуэй>, <Women: Джулия Робертс>, <Women: Ума Турман>...

# >>> Service.objects.exclude(pk=2) => выбирает все записи, которые НЕ соответствуют критерию

# >>> Service.objects.get(pk=2) => выбирает если точно знаем что запись есть, иначе генерирует исключение

# >>> Service.objects.filter(pk__lte=4).order_by('title') - сортировка
# >>> Service.objects.order_by('time_update')
# >>> Service.objects.order_by('-time_update') - обратная сортировка

# >>> wu = Service.objects.get(pk=2)
# >>> wu.tutle = 'Ремонт мониторов' - присваеваем новое значение
# >>> wu.content = 'Качественный ремонт мониторов любой сложности.' - присваеваем новое значение
# >>> wu.save() - сохраняем

# >>> wd = Service.objects.filter(pk__gte=4)
# >>> wd -> <QuerySet [<Service: Ума Турман>, <Women: Кира Найтли>]>
# >>> wd.delete() -> (2, {'service.Service': 2}) - удалили две записи

# http://djbook.ru/rel3.0/topics/db/queries.html