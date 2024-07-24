from django.urls import path
from  . import views

urlpatterns = [
    path('operations/', views.operations, name='operations')
]

