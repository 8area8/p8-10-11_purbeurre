# Generated by Django 3.2.6 on 2021-08-29 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('store', models.CharField(max_length=50)),
                ('url', models.URLField(max_length=255)),
                ('grade', models.CharField(max_length=1)),
                ('image', models.CharField(max_length=255)),
                ('salt', models.FloatField(null=True)),
                ('carbohydrates', models.FloatField(null=True)),
                ('sugars', models.FloatField(null=True)),
                ('fats', models.FloatField(null=True)),
                ('proteins', models.FloatField(null=True)),
                ('categories', models.ManyToManyField(to='snacks.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Substitute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='snacks.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
