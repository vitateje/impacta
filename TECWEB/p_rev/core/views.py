from django.shortcuts import render,redirect
from core.cpf import CPF
from django.http import HttpResponse

def index(request):
    if (request.method == 'GET'):
        pessoaFisica = CPF(request.GET.get ('CPF'))
        if (pessoaFisica.isValid()):
            return render(request, 'index.html')
    
    return redirect('http://127.0.0.1:8000/')
    
def login(request):
    return render(request, 'login.html')


# Create your views here.
