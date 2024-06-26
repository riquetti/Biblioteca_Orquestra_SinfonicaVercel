# Generated by Django 4.2.11 on 2024-05-05 20:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0039_alter_emprestimos_data_emprestimo'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='observacoes_gerais',
            field=models.CharField(blank=True, max_length=200, verbose_name='Observações gerais'),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 5, 17, 51, 9, 799636)),
        ),
        migrations.AlterField(
            model_name='livros',
            name='observacao',
            field=models.CharField(blank=True, max_length=200, verbose_name='Observação'),
        ),
    ]
