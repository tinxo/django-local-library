# Generated by Django 2.1.2 on 2018-11-07 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20181106_1852'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'permissions': (('can_add_mod_del_authors', 'Add, modify or delete authors'),)},
        ),
    ]