# Generated by Django 5.1.3 on 2024-11-27 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_uf_alter_areadosaber_options_alter_avaliacao_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='aluno',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.aluno', verbose_name='Aluno'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='disciplina',
            name='aluno',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.aluno', verbose_name='Aluno'),
            preserve_default=False,
        ),
    ]
