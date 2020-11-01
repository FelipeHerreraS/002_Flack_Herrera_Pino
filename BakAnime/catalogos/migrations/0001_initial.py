# Generated by Django 3.1.2 on 2020-11-01 01:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('tituloPag', models.TextField(max_length=200, null=True)),
                ('sinopsis', models.TextField(max_length=500, null=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('capitulos', models.CharField(max_length=20, null=True)),
                ('duracion', models.CharField(max_length=20, null=True)),
                ('año', models.IntegerField(null=True)),
                ('peso', models.CharField(max_length=20, null=True)),
                ('subtitulos', models.CharField(max_length=200, null=True)),
                ('calidad', models.CharField(max_length=200, null=True)),
                ('formato', models.CharField(max_length=30, null=True)),
                ('tipo', models.CharField(max_length=20, null=True)),
                ('desnudos', models.CharField(max_length=2, null=True)),
                ('censura', models.CharField(max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('description', models.TextField(max_length=800)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalogos.anime')),
            ],
        ),
        migrations.AddField(
            model_name='anime',
            name='generos',
            field=models.ManyToManyField(to='catalogos.Genero'),
        ),
    ]