# Generated by Django 3.2.6 on 2021-08-26 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='stripe_customer',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
