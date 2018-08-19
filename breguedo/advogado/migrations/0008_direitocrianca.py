# Generated by Django 2.0 on 2018-04-03 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advogado', '0007_auto_20180402_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='direitoCrianca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(max_length=800)),
                ('texto', models.TextField()),
                ('imagem', models.ImageField(blank=True, upload_to='img_dirCrianca')),
                ('pub_date', models.DateTimeField(verbose_name='data de publicacao')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advogado.Categoria')),
            ],
        ),
    ]
