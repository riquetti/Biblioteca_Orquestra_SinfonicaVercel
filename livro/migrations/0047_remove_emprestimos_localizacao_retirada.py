# Generated by Django 4.2.13 on 2024-05-22 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0046_remove_emprestimos_tempo_duracao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimos',
            name='localizacao_retirada',
        ),
    ]
