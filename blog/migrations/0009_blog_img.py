# Generated by Django 2.1 on 2019-07-31 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180426_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
