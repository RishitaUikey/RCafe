# Generated by Django 5.0.6 on 2024-07-02 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_alter_purchase_entry_date_alter_purchase_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='item',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]