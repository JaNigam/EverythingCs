# Generated by Django 3.1 on 2020-10-02 18:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_postcomments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='postComments',
            new_name='BlogComment',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='SrNo',
            new_name='sno',
        ),
    ]