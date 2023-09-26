# Generated by Django 4.1.7 on 2023-09-26 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewery_map', '0015_alter_brewery_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewery',
            name='category',
            field=models.CharField(choices=[('Cafe', 'Cafe'), ('Quick Eats', 'Quick Eats'), ('Cocktails 🍸', 'Cocktails 🍸'), ('Fancy Dinner 🍽️', 'Fancy Dinner 🍽️'), ('Casual Dinner 🍴', 'Casual Dinner 🍴'), ('Pub 🍺', 'Pub 🍺'), ('Brewery 🍺', 'Brewery 🍺'), ('Brunch 🍳', 'Brunch 🍳')], default='undefined', max_length=20),
        ),
    ]
