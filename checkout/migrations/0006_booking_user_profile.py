# Generated by Django 3.2.6 on 2021-08-21 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('checkout', '0005_alter_booking_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='profiles.userprofile'),
        ),
    ]
