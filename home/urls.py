from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('predict', views.predictPage, name='predict'),
    path('images', views.viewPage, name='db'),
    path('blog', views.blogPage, name='blog'),
]
