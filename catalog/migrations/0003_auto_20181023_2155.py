# Generated by Django 2.1.2 on 2018-10-24 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20181023_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='lenguaje',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Lenguaje'),
        ),
        migrations.AlterField(
            model_name='lenguaje',
            name='name',
            field=models.CharField(help_text='Select a language for this book', max_length=50, verbose_name='Lenguaje'),
        ),
    ]
