# Generated by Django 3.2.19 on 2023-07-01 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[(0, ''), (1, 'Bad'), (2, 'Not good'), (3, 'Neutral'), (4, 'Good'), (5, 'Really good')], default='0', max_length=255),
        ),
    ]
