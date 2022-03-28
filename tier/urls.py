from django.urls import path
from . import views

urlpatterns = [
    path('', views.tier_index, name='tier_index'),
    path('article/<str:name>/', views.article, name='article'),
]