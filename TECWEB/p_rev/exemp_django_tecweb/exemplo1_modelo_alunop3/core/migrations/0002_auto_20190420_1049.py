# Generated by Django 2.2 on 2019-04-20 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(blank=True)),
            ],
            options={
                'managed': True,
                'db_table': 'core_disciplina',
            },
        ),
        migrations.AlterModelOptions(
            name='aluno',
            options={'managed': True},
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='id',
        ),
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='aluno',
            table='core_aluno',
        ),
    ]