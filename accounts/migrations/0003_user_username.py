# Generated by Django 3.0.2 on 2020-02-02 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200201_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
