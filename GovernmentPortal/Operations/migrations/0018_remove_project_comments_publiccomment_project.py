# Generated by Django 4.1.2 on 2022-10-30 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Operations', '0017_publiccomment_project_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='comments',
        ),
        migrations.AddField(
            model_name='publiccomment',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Operations.project'),
        ),
    ]
