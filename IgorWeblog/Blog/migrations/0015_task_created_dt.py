# Generated by Django 4.0.5 on 2022-07-02 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0014_remove_task_created_dt_alter_task_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_dt',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата'),
        ),
    ]
