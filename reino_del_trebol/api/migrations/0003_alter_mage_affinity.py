# Generated by Django 5.0.6 on 2024-07-05 00:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_mage_table_alter_magicaffinity_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mage',
            name='affinity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='affinities', to='api.magicaffinity'),
        ),
    ]
