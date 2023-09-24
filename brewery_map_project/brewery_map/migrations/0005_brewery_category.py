# Generated by Django 4.1.7 on 2023-09-24 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewery_map', '0004_brewery_yelp'),
    ]

    operations = [
        migrations.AddField(
            model_name='brewery',
            name='category',
            field=models.CharField(choices=[('cafe', 'Coffee Shop'), ('quick bite', 'quick bite'), ('drinks', 'drinks'), ('fine dining', 'fine dining'), ('pub', 'pub'), ('brewery', 'brewery')], default='undefined', max_length=20),
        ),
    ]