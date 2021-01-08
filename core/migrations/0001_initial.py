# Generated by Django 3.1.4 on 2020-12-10 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(blank=True, max_length=100, null=True)),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
                ('bairro', models.CharField(blank=True, max_length=50, null=True)),
                ('cidade', models.CharField(blank=True, max_length=100, null=True)),
                ('cep', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.CharField(max_length=100)),
                ('telefone', models.CharField(blank=True, max_length=30, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos_clientes')),
            ],
        ),
    ]
