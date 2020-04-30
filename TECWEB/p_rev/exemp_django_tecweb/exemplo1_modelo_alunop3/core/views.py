from django.shortcuts import render,redirect
from core.models import Aluno, Disciplina


# Create your views here.
def index(request):
    ctx = {
        "materia":"TecWeb AC06"
    }
    return render(request,"index.html",ctx)
def cadastro_aluno(request):
    return render(request,"cadastro_aluno.html")

def novo_aluno(request):
    nome = request.POST.get("nome")
    nota = request.POST.get("nota")
    Aluno.objects.create(nome = nome , nota = nota)
    return redirect("/")

def consulta_aluno(request):
        aluno = Aluno.objects.all()
        return render (request,'consulta_aluno.html',{'aluno': aluno} )

def cad_disciplina(request): # teste vitor
    return render(request, "cad_disciplina.html")

def consulta_disciplina(request):
     context = request.POST.get('nome')
     return render (request,'consulta_disciplina.html',{'nome': context} )

def consultaok(request):
     context = request.POST.get('nome')
     return render (request,'consulta_disciplina.html',{'nome': context} )

def nova_disciplina(request):
    nome = request.POST.get('nome')
    nota = request.POST.get("nota")
    Disciplina.objects.create(nome=nome, nota = nota)
    return redirect('/')

