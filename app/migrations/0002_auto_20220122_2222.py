# Generated by Django 2.2.26 on 2022-01-22 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apps',
            name='domain_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='apps',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
