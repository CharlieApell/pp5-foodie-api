# Generated by Django 3.2.19 on 2023-06-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230612_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_rgq6aq', upload_to='images/'),
        ),
    ]
