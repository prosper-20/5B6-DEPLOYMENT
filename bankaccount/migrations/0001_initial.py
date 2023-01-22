# Generated by Django 4.1.5 on 2023-01-17 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bvn', models.BigIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('account_number', models.BigIntegerField()),
                ('balance', models.FloatField()),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
            ],
        ),
    ]