# Generated by Django 4.2.2 on 2023-08-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0031_remove_package_end_date_remove_package_start_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='duration',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
