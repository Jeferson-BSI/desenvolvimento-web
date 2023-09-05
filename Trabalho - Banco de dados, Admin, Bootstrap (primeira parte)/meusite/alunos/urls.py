from django.urls import path
from . import views
from django.shortcuts import redirect


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:aluno_id>/', views.aluno_detail, name='aluno_detail'),
    path('contato/', views.contato, name='contato'),
]
