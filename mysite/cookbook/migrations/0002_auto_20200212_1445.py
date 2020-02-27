# Generated by Django 3.0.3 on 2020-02-12 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no category', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cookbook.RecipeType'),
        ),
    ]
