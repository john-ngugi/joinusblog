# Generated by Django 4.0.4 on 2022-10-15 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
