# Generated by Django 3.0.3 on 2020-02-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0002_auto_20200212_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(default='none specified', max_length=2000),
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]
