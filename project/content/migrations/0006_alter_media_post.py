# Generated by Django 5.0.4 on 2024-05-31 10:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_remove_media_image_media_file_type_alter_media_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='content.post'),
        ),
    ]
