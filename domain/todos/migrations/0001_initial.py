# Generated by Django 4.1 on 2023-05-02 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('todo', 'To Do'), ('done', 'Done')], default='todo', max_length=10)),
                ('notes', models.TextField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='guests.guest')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
