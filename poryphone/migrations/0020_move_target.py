# Generated by Django 2.2.4 on 2019-11-02 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poryphone', '0019_target'),
    ]

    operations = [
        migrations.AddField(
            model_name='move',
            name='target',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='poryphone.Target'),
        ),
    ]
