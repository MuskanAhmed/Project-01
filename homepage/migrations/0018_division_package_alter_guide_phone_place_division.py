# Generated by Django 4.2.2 on 2023-08-07 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0017_alter_guide_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('DHAKA', 'Dhaka Division'), ('BARISAL', 'Barisal Division'), ('KHULNA', 'Khulna Divison'), ('MYMENSINGH', 'Mymensingh Division'), ('RAJSHAHI', 'Rajshahi Division'), ('RANGPUR', 'Rangpur Divison'), ('SYLHET', 'Sylhet Division'), ('CHITTAGONG', 'Chittagong')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('source', models.CharField(max_length=100, null=True)),
                ('destination', models.CharField(max_length=100, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('plan', models.TextField(null=True)),
                ('terms', models.TextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='guide',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='division',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.division'),
        ),
    ]