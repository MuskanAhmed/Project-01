# Generated by Django 4.2.2 on 2023-08-06 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='TourPackage',
            new_name='Place',
        ),
        migrations.CreateModel(
            name='PlaceVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.URLField(null=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.place')),
            ],
        ),
        migrations.CreateModel(
            name='PlaceFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='placeimage/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.place')),
            ],
        ),
        migrations.CreateModel(
            name='PlaceCulture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='placeimage/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.place')),
            ],
        ),
        migrations.CreateModel(
            name='HotelPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='hotelimage/')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.hotel')),
            ],
        ),
    ]
