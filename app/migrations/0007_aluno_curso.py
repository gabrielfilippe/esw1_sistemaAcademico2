# Generated by Django 5.1.4 on 2025-01-14 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_pessoa_idade'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.curso', verbose_name='Curso'),
            preserve_default=False,
        ),
    ]
