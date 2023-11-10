from django.urls import path
from .views import Index, home
urlpatterns = [
    path('tarjimon/', Index, name="index"),
    path('', home, name="home"),

]