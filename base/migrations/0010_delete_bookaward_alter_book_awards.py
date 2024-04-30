# Generated by Django 5.0.3 on 2024-04-26 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_book_published_alter_book_publisher'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookAward',
        ),
        migrations.AlterField(
            model_name='book',
            name='awards',
            field=models.ManyToManyField(blank=True, null=True, to='base.authoraward'),
        ),
    ]
