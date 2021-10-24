# Generated by Django 3.2.8 on 2021-10-24 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='id_games',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='id_game', to='api.game'),
            preserve_default=False,
        ),
    ]
