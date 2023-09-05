from django.shortcuts import render, get_object_or_404
from .models import Aluno, PaginaInicial
from .forms import ContatoForm

def pagina_inicial(request):
    return render(request, 'alunos/pagina_inicial.html')


def aluno_detail(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    return render(request, 'alunos/aluno_detail.html', {'aluno': aluno})



def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            # Processar o formulário, enviar e-mail, etc.
            # Exibir informações no terminal como simulado
            print("Nome Completo:", form.cleaned_data['nome_completo'])
            print("Email:", form.cleaned_data['email'])
            print("Mensagem:", form.cleaned_data['mensagem'])
    else:
        form = ContatoForm()
    return render(request, 'alunos/contato.html', {'form': form})


def index(request):
    pagina_inicial = PaginaInicial.objects.first()
    alunos = Aluno.objects.all()
    return render(request, 'alunos/index.html', {'pagina_inicial': pagina_inicial, 'alunos': alunos})