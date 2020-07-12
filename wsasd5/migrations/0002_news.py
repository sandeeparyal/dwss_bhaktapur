# Generated by Django 3.0.5 on 2020-07-12 11:46

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wsasd5', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('published_date', models.DateTimeField()),
                ('short_text', models.CharField(max_length=120)),
            ],
        ),
    ]
