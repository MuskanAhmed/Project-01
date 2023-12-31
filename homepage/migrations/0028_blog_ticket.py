# Generated by Django 4.2.2 on 2023-08-13 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0027_package_remaining_seats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='blog/')),
                ('upload_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(choices=[('Hanif', 'Hanif'), ('Ena', 'Ena'), ('Bashumati', 'Bashumati')], max_length=30, null=True)),
                ('source', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Chattogram', 'Chattogram'), ('Nārāyanganj', 'Nārāyanganj'), ('Khulna', 'Khulna'), ('Gāzipura', 'Gāzipura'), ('Rangapukur', 'Rangapukur'), ('Mymensingh', 'Mymensingh'), ('Bogra', 'Bogra'), ('Tungi', 'Tungi'), ('Siddhirganj', 'Siddhirganj'), ('Narsingdi', 'Narsingdi'), ('Sirajganj', 'Sirajganj')], max_length=20, null=True)),
                ('destination', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Chattogram', 'Chattogram'), ('Nārāyanganj', 'Nārāyanganj'), ('Khulna', 'Khulna'), ('Gāzipura', 'Gāzipura'), ('Rangapukur', 'Rangapukur'), ('Mymensingh', 'Mymensingh'), ('Bogra', 'Bogra'), ('Tungi', 'Tungi'), ('Siddhirganj', 'Siddhirganj'), ('Narsingdi', 'Narsingdi'), ('Sirajganj', 'Sirajganj')], max_length=20, null=True)),
                ('going_date', models.DateField(null=True)),
                ('return_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
