
from django.urls import path
from . import views

urlpatterns = [
    path('all_meals/', views.meal, name = 'all_meals'),
]
