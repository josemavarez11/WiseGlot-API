# Generated by Django 5.0.4 on 2024-07-30 15:06

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('des_profile', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('des_subscription', models.CharField(max_length=90)),
                ('pri_subscription', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
            options={
                'db_table': 'subscription',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nam_user', models.CharField(max_length=300)),
                ('ema_user', models.CharField(max_length=300, unique=True)),
                ('pas_user', models.CharField(max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('profile_img_url', models.CharField(default='https://w7.pngwing.com/pngs/81/570/png-transparent-profile-logo-computer-icons-user-user-blue-heroes-logo.png')),
                ('id_profile_user', models.ForeignKey(default='5eab56af-60f5-4290-af60-a0dda32ee1af', on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('id_subscription_user', models.ForeignKey(default='b6f69838-82c8-454e-9937-9ab61d235400', on_delete=django.db.models.deletion.CASCADE, to='users.subscription')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
