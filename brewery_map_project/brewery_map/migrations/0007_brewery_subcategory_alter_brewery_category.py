# Generated by Django 4.1.7 on 2023-09-24 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewery_map', '0006_alter_brewery_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='brewery',
            name='subcategory',
            field=models.CharField(choices=[('Mediterranean', 'Mediterranean'), ('Italian', 'Italian'), ('American', 'American'), ('Live Music', 'Live Music'), ('Funky', 'Funky')], default='undefined', max_length=20),
        ),
        migrations.AlterField(
            model_name='brewery',
            name='category',
            field=models.CharField(choices=[('Coffee/Work/Reading', 'Coffee'), ('Quick Eats', 'Lunch'), ('Cocktails', 'cocktails'), ('Fancy Dinner', 'Fancy Dinner'), ('Casual Dinner', 'Casual Dinner'), ('Pub', 'Pub'), ('Brewery', 'Brewery'), ('Brunch', 'Brunch')], default='undefined', max_length=20),
        ),
    ]