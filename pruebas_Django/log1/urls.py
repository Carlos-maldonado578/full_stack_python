from django.urls import path
from . import views
urlpatterns = [
    path('', views.root),
    path('blog/', views.blogs),
    path('blog/new/', views.new),
    path('blog/create', views.create),
    path('blog/<int:_numero>', views.show),
    path('blog/<_numero>/edit', views.edit),
    path('blog/<_numero>/delete',views.delete),
    path('blogs/json', views.json)
]