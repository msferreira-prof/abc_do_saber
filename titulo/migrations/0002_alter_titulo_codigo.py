# Generated by Django 5.1 on 2024-08-26 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titulo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titulo',
            name='codigo',
            field=models.AutoField(help_text='Código do Tipo do Título', primary_key=True, serialize=False),
        ),
    ]
