# Generated by Django 4.1.7 on 2023-09-24 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewery_map', '0007_brewery_subcategory_alter_brewery_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewery',
            name='subcategory',
            field=models.CharField(choices=[('Mediterranean', 'Mediterranean'), ('Italian', 'Italian'), ('American', 'American'), ('Live Music', 'Live Music'), ('Funky', 'Funky'), ('Lots of Options', 'Lots of Options')], default='undefined', max_length=20),
        ),
    ]
