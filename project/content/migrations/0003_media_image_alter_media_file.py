# Generated by Django 5.0.4 on 2024-05-27 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_comment_acception_alter_comment_post_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='image',
            field=models.ImageField(default=None, upload_to='images', verbose_name='Изображения'),
        ),
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(upload_to='files', verbose_name='Файл'),
        ),
    ]
