# Generated by Django 3.0.2 on 2020-02-04 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chanel', '0005_auto_20200204_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chanel',
            name='law',
            field=models.TextField(max_length=2000),
        ),
    ]
