# Generated by Django 3.2.5 on 2021-08-02 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0005_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
