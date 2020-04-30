# Generated by Django 2.1.7 on 2019-04-29 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190420_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='nota',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='nota'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='nome',
            field=models.TextField(blank=True, verbose_name='nome_disciplina'),
        ),
    ]