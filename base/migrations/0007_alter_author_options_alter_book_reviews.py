# Generated by Django 5.0.3 on 2024-04-26 06:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_author_middle_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['first_name', 'middle_name', 'last_name', 'gender']},
        ),
        migrations.AlterField(
            model_name='book',
            name='reviews',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.review'),
        ),
    ]
