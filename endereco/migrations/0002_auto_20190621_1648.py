# Generated by Django 2.0.1 on 2019-06-21 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='linha2',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
