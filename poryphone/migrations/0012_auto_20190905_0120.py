# Generated by Django 2.2.4 on 2019-09-05 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poryphone', '0011_auto_20190904_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='pokemon',
            field=models.ManyToManyField(related_name='family_pokemon', to='poryphone.Pokemon'),
        ),
    ]
