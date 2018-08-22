# Generated by Django 2.1 on 2018-08-21 17:56

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='video_url',
        ),
        migrations.AddField(
            model_name='lesson',
            name='video',
            field=embed_video.fields.EmbedVideoField(null=True),
        ),
    ]
