# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# # Create your views here.
# from django.shortcuts import render, redirect
# from .models import Aluno
# from .forms import AlunoForm

# def cadastro_aluno(request):
#     if not request.user.is_authenticated:
#         return redirect('index')
    
#     if request.method == 'POST':
#         form = AlunoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('alunos_cadastrados')
#     else:
#         form = AlunoForm()
    
#     return render(request, 'alunos/cadastro_aluno.html', {'form': form})

def alunos_cadastrados(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/alunos_cadastrados.html', {'alunos': alunos})

from django.shortcuts import render, redirect
from .forms import AlunoForm
from .models import Aluno

def index(request):
    return render(request, 'index.html')

def cadastro_aluno(request):
    if not request.user.is_authenticated:
        return redirect('index')  # Redirecionar para a página de login ou index

    if request.method == 'POST':
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirecionar após o cadastro bem-sucedido

    else:
        form = AlunoForm()

    return render(request, 'cadastro_aluno.html', {'form': form})


def alunos_cadastrados(request):
    if not request.user.is_authenticated:
        return redirect('index')  # Redirecionar para a página de login ou index

    alunos = Aluno.objects.all()
    return render(request, 'alunos_cadastrados.html', {'alunos': alunos})