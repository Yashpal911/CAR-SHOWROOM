# Generated by Django 2.2.2 on 2020-05-04 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_auto_20200504_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='enquery_date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='remark_date',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
