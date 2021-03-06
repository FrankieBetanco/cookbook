# Generated by Django 3.0.3 on 2020-02-27 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0004_auto_20200217_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='comment',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default='none specified', max_length=2000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(max_length=2000),
        ),
    ]
