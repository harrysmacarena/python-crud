# Generated by Django 3.1 on 2020-10-03 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedor', '0003_tabla_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tabla_test1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('columna_uno', models.CharField(max_length=200)),
                ('columna_dos', models.CharField(max_length=200)),
                ('columna_tres', models.CharField(max_length=200)),
                ('columna_cuatro', models.CharField(max_length=200)),
            ],
        ),
    ]
