# Generated by Django 5.0.2 on 2024-03-01 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReversedIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_ip', models.CharField(max_length=15)),
                ('reversed_ip', models.CharField(max_length=15)),
            ],
        ),
    ]