# Generated by Django 3.2.5 on 2021-07-24 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_rename_urlfiled_project_urlfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='URLField',
            field=models.URLField(blank=True, null=True),
        ),
    ]