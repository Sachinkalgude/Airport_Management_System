# Generated by Django 4.2.3 on 2023-10-03 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flights', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flights',
            name='Flight_no',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
