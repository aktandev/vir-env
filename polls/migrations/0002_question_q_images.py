# Generated by Django 4.0.4 on 2022-06-01 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='q_images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
