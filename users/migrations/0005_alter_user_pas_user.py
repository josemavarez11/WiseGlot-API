# Generated by Django 5.0.4 on 2024-05-13 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_subscription_des_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pas_user',
            field=models.CharField(max_length=120),
        ),
    ]
