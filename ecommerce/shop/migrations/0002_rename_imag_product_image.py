# Generated by Django 3.2.8 on 2021-11-24 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='imag',
            new_name='image',
        ),
    ]
