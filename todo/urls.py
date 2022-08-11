from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoIndex.as_view(), name='index'),
]
