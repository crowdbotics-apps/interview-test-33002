# Generated by Django 2.2.26 on 2022-01-22 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220122_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='apps',
            name='screenshot',
            field=models.ImageField(default='app/screenshots/default.jpg', upload_to='app/screenshot/default.jpg'),
        ),
    ]
