# Generated by Django 4.2.11 on 2025-03-15 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='updated_at',
            new_name='updated',
        ),
    ]
