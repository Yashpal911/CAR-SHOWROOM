# Generated by Django 2.2.6 on 2020-05-04 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0008_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='img1',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='about',
            name='img2',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
