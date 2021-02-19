from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('random_word', views.random_word),
    path('success', views.success),
]