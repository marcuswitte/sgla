from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0007_alter_livro_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='prioridade',
            new_name='lingua',
        ),
    ]
