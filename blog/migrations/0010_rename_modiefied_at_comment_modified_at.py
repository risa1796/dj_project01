# Generated by Django 3.2.14 on 2022-08-17 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='modiefied_at',
            new_name='modified_at',
        ),
    ]
