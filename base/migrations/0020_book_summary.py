# Generated by Django 5.0.3 on 2024-04-28 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_librayrecords_return_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
