# Generated by Django 5.0.3 on 2024-04-28 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_librayrecords_projected_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librayrecords',
            name='projected_date',
            field=models.DateTimeField(null=True),
        ),
    ]
