# Generated by Django 3.2.11 on 2022-01-27 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='eintrag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateTimeField()),
                ('beschreibung', models.CharField(max_length=200)),
            ],
        ),
    ]
