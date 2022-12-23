# Generated by Django 4.1.4 on 2022-12-23 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('ethnicity', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=32)),
                ('hobbies', models.TextField()),
                ('occupation', models.CharField(max_length=32)),
                ('image', models.TextField()),
            ],
        ),
    ]
