# Generated by Django 5.0.3 on 2024-04-28 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_librayrecords_return_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='awards',
            field=models.ManyToManyField(blank=True, to='base.authoraward'),
        ),
        migrations.AlterField(
            model_name='book',
            name='awards',
            field=models.ManyToManyField(blank=True, to='base.authoraward'),
        ),
    ]
