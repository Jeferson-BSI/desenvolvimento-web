from django.urls import path
from . import views

urlpatterns = [
    # path('cadastro/', views.cadastro_aluno, name='cadastro_aluno'),
    path('alunos_cadastrados/', views.alunos_cadastrados, name='alunos_cadastrados'),
    path('cadastro_aluno/', views.cadastro_aluno, name='cadastro_aluno'),
    path('', views.index, name='index'),  # Configuração da URL para a página inicial


]
