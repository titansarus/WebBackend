# Generated by Django 3.0.2 on 2020-02-03 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_user_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(max_length=1000, null=True, upload_to='profile/'),
        ),
    ]