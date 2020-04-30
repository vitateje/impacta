from django.db import models


# Create your models here.
class Aluno(models.Model):
    nome = models.CharField("nome",max_length=50)
    matricula = models.AutoField(primary_key=True)
    nota = models.DecimalField("nota",max_digits=10,decimal_places=2)

    class Meta:
        managed = True
        db_table = 'core_aluno'

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    disciplina = models.AutoField(primary_key=True)
    nome = models.TextField("nome", blank=True, null=False)
    nota = models.DecimalField("nota",max_digits=10,decimal_places=2)

    class Meta:
        managed = True
        db_table = 'core_disciplina'

    def __str__(self):
        return self.nome