# lugat
django-install
>>pip install pipenv
>>pipenv shell
>>pipenv install django
>>django-admin --version
>>django-admin startproject project_name
>>cd project_name 
>>py manage.py runserver
>>CTRL+C
>>py manage.py startapp myapp
1- create settings add myapp-->

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Myapp.apps.MyappConfig', #add myapp <<---
]
