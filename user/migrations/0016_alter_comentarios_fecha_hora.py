# Generated by Django 5.1 on 2024-09-22 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_alter_user_location_alter_user_number_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='fecha_hora',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
