# Generated by Django 2.2.28 on 2023-11-19 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_actif_etat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portefeuille',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('argent_disponible', models.FloatField(default=10000.0)),
            ],
        ),
    ]
