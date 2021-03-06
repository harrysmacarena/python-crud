# Generated by Django 3.1 on 2020-09-04 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcom', models.CharField(max_length=200)),
                ('nombre', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idcom', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.DateTimeField(verbose_name='Nombre Region')),
            ],
            options={
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='Region1',
            fields=[
                ('idcom', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.DateTimeField(verbose_name='Nombre Region')),
            ],
            options={
                'db_table': 'harrisito',
            },
        ),
        migrations.CreateModel(
            name='Region2',
            fields=[
                ('idcom', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.DateTimeField(verbose_name='Nombre Region')),
            ],
            options={
                'db_table': 'harrixxx',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('idprov', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.DateTimeField(verbose_name='Nombre Provincia')),
                ('idRegion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenedor.region')),
            ],
            options={
                'db_table': 'provincia',
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenedor.poll')),
            ],
        ),
    ]
