# Generated by Django 5.1.5 on 2025-02-12 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_core', '0002_alter_publisher_address_alter_publisher_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='first_name',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='last_name',
            new_name='name',
        ),
    ]
