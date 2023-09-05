from django import forms

class ContatoForm(forms.Form):
    nome_completo = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)
