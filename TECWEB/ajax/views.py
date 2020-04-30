from django.shortcuts import render,redirect
from core.models import Aluno,Disciplina,Turma
from django.views.generic import View,TemplateView,ListView
from django.utils.text import slugify
from django.http import HttpResponse
import json
from decimal import Decimal

# Create your views here.
class IndexView(object):
    def __call__(self,request):
        ctx = {
            "aluno":"Ramon"
        }
        return render(request,"base.html",ctx)

index = IndexView()

class AlunoView(ListView):
    template_name = "consulta_aluno.html"
    context_object_name = "aluno"    
    def get_queryset(self):
        return Aluno.objects.get(nome = self.kwargs["slug"])                
            
consulta_aluno = AlunoView.as_view()

class AlunosView(ListView):
    model = Aluno
    context_object_name = "alunos"
    template_name = "consulta_alunos.html"

consulta_alunos = AlunosView.as_view()

def consulta_ajax_aluno(request):
    aluno_dicionario = json.loads(request.body.decode('utf-8'))
    aluno = Aluno.objects.get(nome = aluno_dicionario["nome"])
    aluno_resposta = {
        "nome": aluno.nome,
        "matricula": aluno.matricula,
        "nota": aluno.nota
    }
    response = HttpResponse(
        json.dumps(aluno_resposta, cls=DecimalEncoder)
        ,content_type='application/json'
    )
    return response

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)
