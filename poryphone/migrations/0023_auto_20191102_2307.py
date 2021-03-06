# Generated by Django 2.2.4 on 2019-11-03 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poryphone', '0022_auto_20191102_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='pokemon',
        ),
        migrations.AddField(
            model_name='syncpair',
            name='base_potential',
            field=models.IntegerField(blank=True, default=3, null=True),
        ),
        migrations.AddField(
            model_name='syncpair',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poryphone.Role'),
        ),
        migrations.AddField(
            model_name='syncpair',
            name='trainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poryphone.Trainer'),
        ),
    ]
