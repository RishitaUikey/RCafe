# Generated by Django 5.0.6 on 2024-07-01 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_ainventory_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ainventory',
            name='expiry_date',
            field=models.DateField(null=True),
        ),
    ]