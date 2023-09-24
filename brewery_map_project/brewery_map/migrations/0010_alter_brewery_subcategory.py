# Generated by Django 4.1.7 on 2023-09-24 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewery_map', '0009_alter_brewery_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewery',
            name='subcategory',
            field=models.CharField(choices=[('Mediterranean', 'Mediterranean'), ('Italian', 'Italian'), ('American', 'American'), ('Live Music', 'Live Music'), ('Funky', 'Funky'), ('Lots of Options', 'Lots of Options'), ('Cool Experience', 'Cool Experience'), ('N/A', 'N/A')], default='undefined', max_length=20),
        ),
    ]
