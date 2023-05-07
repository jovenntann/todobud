# Generated by Django 4.1 on 2023-05-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_alter_todo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='duration',
            field=models.PositiveIntegerField(default=0, help_text='Duration in minutes'),
        ),
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], default='medium', max_length=10),
        ),
        migrations.AddField(
            model_name='todo',
            name='time_spent',
            field=models.PositiveIntegerField(default=0, help_text='Time spent in minutes'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('todo', 'Todo'), ('pending', 'Pending'), ('in_progress', 'In Progress'), ('done', 'Done')], default='todo', max_length=15),
        ),
    ]
