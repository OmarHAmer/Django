# Generated by Django 4.1 on 2022-08-08 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('job_type', models.CharField(choices=[('F', 'Full Time'), ('P', 'Part Time')], max_length=20)),
                ('description', models.TextField(max_length=1000)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('vacancy', models.IntegerField(default=1)),
                ('salary', models.IntegerField()),
                ('experience', models.IntegerField(default=0)),
            ],
        ),
    ]
