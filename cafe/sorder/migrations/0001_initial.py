# Generated by Django 5.0.6 on 2024-06-11 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('food_item', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
    ]
