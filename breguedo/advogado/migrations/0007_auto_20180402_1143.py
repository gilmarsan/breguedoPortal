# Generated by Django 2.0 on 2018-04-02 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advogado', '0006_contato'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='fone_celular',
            new_name='celular',
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='cep_contato',
            new_name='cep',
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='cidade_contato',
            new_name='cidade',
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='email_contato',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='end_contato',
            new_name='endereço',
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='estado_contato',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='txt_mensagem',
            new_name='mensagem',
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='nome_contato',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='fone_comercial',
            new_name='tel_comercial',
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='fone_residencial',
            new_name='tel_residencial',
        ),
    ]
