# Generated by Django 4.2.2 on 2023-08-13 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0029_blog_author_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='package_name',
        ),
        migrations.AddField(
            model_name='review',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.package'),
        ),
    ]