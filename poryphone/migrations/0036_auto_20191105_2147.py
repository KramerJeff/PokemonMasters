# Generated by Django 2.2.4 on 2019-11-06 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poryphone', '0035_auto_20191105_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
