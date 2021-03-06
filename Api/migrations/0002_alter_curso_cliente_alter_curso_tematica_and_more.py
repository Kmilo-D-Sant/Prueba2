# Generated by Django 4.0.2 on 2022-04-14 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='Cliente',
            field=models.ManyToManyField(through='Api.NotasCurso', to='Api.Cliente'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='Tematica',
            field=models.ManyToManyField(to='Api.Tematica'),
        ),
        migrations.AlterField(
            model_name='normacuba',
            name='iso',
            field=models.ManyToManyField(to='Api.Isos'),
        ),
    ]
