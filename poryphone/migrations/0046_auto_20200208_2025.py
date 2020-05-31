# Generated by Django 2.2.4 on 2020-02-09 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poryphone', '0045_syncmove_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='syncpairmove',
            options={'ordering': ['syncpair']},
        ),
        migrations.AlterField(
            model_name='syncmove',
            name='syncpair',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sp_syncmove', to='poryphone.SyncPair'),
        ),
        migrations.AlterField(
            model_name='syncpairmove',
            name='move',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spmoves', to='poryphone.Move'),
        ),
        migrations.AlterField(
            model_name='syncpairmove',
            name='syncpair',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spmoves', to='poryphone.SyncPair'),
        ),
        migrations.AlterField(
            model_name='syncpairpassive',
            name='passive',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_syncpairpassive', to='poryphone.Passive'),
        ),
        migrations.AlterField(
            model_name='syncpairpassive',
            name='syncpair',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sp_syncpairpassive', to='poryphone.SyncPair'),
        ),
    ]
