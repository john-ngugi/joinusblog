# Generated by Django 4.0.4 on 2022-10-15 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_post_titlebreak1_alter_post_titlebreak2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
