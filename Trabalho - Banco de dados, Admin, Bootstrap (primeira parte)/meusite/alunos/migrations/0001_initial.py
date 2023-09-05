# Generated by Django 4.2.1 on 2023-09-05 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('matricula', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('periodo_ingresso', models.DateField()),
                ('notaweb_avancado', models.IntegerField()),
                ('situacao', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PaginaInicial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
            ],
        ),
    ]