# Generated by Django 5.0.6 on 2024-06-24 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiService', '0002_alter_file_parent_alter_folder_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='files',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='folders',
        ),
    ]
