# Generated by Django 5.0.4 on 2024-04-28 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_menuitem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='nutritional_info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
