# Generated by Django 4.2.7 on 2023-11-28 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tag_id',
            field=models.ManyToManyField(blank=True, related_name='tag', to='Task.tag'),
        ),
    ]
