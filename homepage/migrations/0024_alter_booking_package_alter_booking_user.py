# Generated by Django 4.2.2 on 2023-08-07 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0023_booking_number_booking_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='package',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]