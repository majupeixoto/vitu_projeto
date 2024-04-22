# Generated by Django 5.0.4 on 2024-04-22 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_funcionario_nome_completo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionario',
            name='username',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
