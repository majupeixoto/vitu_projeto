# Generated by Django 5.0.4 on 2024-04-23 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0012_cliente_username_funcionario_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]