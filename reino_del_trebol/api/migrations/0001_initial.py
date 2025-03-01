# Generated by Django 5.0.6 on 2024-07-05 00:28

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MagicAffinity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('magic_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Mage',
            fields=[
                ('id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)])),
                ('status', models.BooleanField(default=False)),
                ('affinity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.magicaffinity')),
            ],
        ),
    ]
