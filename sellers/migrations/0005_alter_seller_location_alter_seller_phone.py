# Generated by Django 4.1.1 on 2022-11-12 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0004_remove_seller_user_id_alter_seller_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='location',
            field=models.CharField(default=1, max_length=25),
        ),
        migrations.AlterField(
            model_name='seller',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
