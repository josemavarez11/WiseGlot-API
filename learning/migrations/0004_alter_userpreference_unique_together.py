# Generated by Django 5.0.4 on 2024-05-19 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0003_alter_userpreferencetopic_unique_together'),
        ('users', '0006_alter_user_id_profile_user_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userpreference',
            unique_together={('id_user', 'id_native_language', 'id_language_to_study', 'id_language_to_study_level', 'id_reason_to_study')},
        ),
    ]
