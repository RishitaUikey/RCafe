# Generated by Django 5.0.6 on 2024-06-15 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('item', models.FloatField(blank=True, null=True)),
                ('unit', models.CharField(max_length=10)),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
                ('expiry_date', models.DateTimeField()),
                ('price', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]