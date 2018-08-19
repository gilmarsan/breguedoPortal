# Generated by Django 2.0 on 2018-04-11 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advogado', '0024_ilustracao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(blank=True, max_length=800)),
                ('texto', models.TextField()),
                ('imagem', models.ImageField(blank=True, upload_to='img_literatura')),
                ('pub_date', models.DateTimeField(verbose_name='data de publicacao')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advogado.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Microconto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80)),
                ('subtitulo', models.CharField(blank=True, max_length=180)),
                ('texto', models.CharField(max_length=560)),
                ('imagem', models.ImageField(blank=True, upload_to='img_literatura')),
                ('pub_date', models.DateTimeField(verbose_name='data de publicacao')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advogado.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Poema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(blank=True, max_length=800)),
                ('texto', models.TextField()),
                ('imagem', models.ImageField(blank=True, upload_to='img_literatura')),
                ('pub_date', models.DateTimeField(verbose_name='data de publicacao')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advogado.Categoria')),
            ],
        ),
        migrations.RenameModel(
            old_name='Juris',
            new_name='Juri',
        ),
        migrations.RemoveField(
            model_name='literatura',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Literatura',
        ),
    ]
