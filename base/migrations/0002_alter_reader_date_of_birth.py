# Generated by Django 5.0.3 on 2024-04-26 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]