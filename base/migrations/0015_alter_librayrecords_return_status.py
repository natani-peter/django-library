# Generated by Django 5.0.3 on 2024-04-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_remove_book_reviews_review_book_alter_review_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librayrecords',
            name='return_status',
            field=models.CharField(blank=True, choices=[('G', 'Good'), ('B', 'Bad')], max_length=250, null=True),
        ),
    ]
