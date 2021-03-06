# Generated by Django 3.1.4 on 2020-12-10 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201210_0013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabricante', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('ano', models.CharField(blank=True, max_length=4, null=True)),
                ('cor', models.CharField(blank=True, max_length=20, null=True)),
                ('placa', models.CharField(max_length=10)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos_veiculos')),
                ('Id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
            ],
            options={
                'verbose_name_plural': 'Veiculos',
            },
        ),
    ]
