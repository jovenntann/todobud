# Generated by Django 4.1 on 2022-12-07 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_alter_store_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
