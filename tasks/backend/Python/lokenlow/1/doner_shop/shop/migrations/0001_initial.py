# Generated by Django 5.1 on 2024-08-10 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(blank=True, default=None, max_length=300, null=True)),
                ('description', models.TextField(blank=True, default=None, max_length=2000, null=True)),
            ],
        ),
    ]
