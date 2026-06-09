from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0003_alter_autor_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='autor',
            name='data_criacao',
        ),
    ]
