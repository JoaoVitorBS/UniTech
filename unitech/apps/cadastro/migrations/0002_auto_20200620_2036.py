# Generated by Django 2.0.13 on 2020-06-20 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='email_responsavel',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
