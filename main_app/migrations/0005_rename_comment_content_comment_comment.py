# Generated by Django 4.1.7 on 2023-03-15 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0004_alter_comment_post"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment", old_name="comment_content", new_name="comment",
        ),
    ]
