# Generated by Django 2.0.3 on 2018-03-31 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artigo_titulo', models.CharField(max_length=200)),
                ('artigo_subtitulo', models.CharField(max_length=800)),
                ('artigo_texto', models.TextField()),
                ('artigo_img', models.ImageField(upload_to='')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria_nome', models.CharField(max_length=80)),
                ('categoria_desc', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='artigo',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advogado.Categoria'),
        ),
    ]
