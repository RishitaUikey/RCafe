# Generated by Django 5.0.6 on 2024-07-02 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_alter_ainventory_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ainventory',
            name='expiry_date',
            field=models.DateField(null=True),
        ),
    ]
