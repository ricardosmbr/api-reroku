# Generated by Django 2.0.1 on 2019-06-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
        ('core', '0003_pontoturistico_atracoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='comentario',
            field=models.ManyToManyField(to='comentarios.Comentario'),
        ),
    ]
