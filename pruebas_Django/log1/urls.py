from django.urls import path
from . import views
urlpatterns = [
    path('', views.root),
    path('blog/', views.index),
    path('blog/new/', views.new),
    path('blog/create/', views.create),
    path('blog/<_numero>', views.show),
    path('blog/<_numero>/editar', views.editar),
    path('blog/<_numero>/delete',views.delete),
    path('blogs/json', views.json)
]