# Generated by Django 2.1.2 on 2018-11-07 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20181107_1706'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('can_add_mod_del_books', 'Add, modify or delete books'),)},
        ),
    ]
