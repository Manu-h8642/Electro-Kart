# Generated by Django 4.2.7 on 2023-12-11 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_pdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdb',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pdb',
            name='desc',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
