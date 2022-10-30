# Generated by Django 4.1.2 on 2022-10-29 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('registration_no', models.TextField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('user_type', models.CharField(choices=[(1, 'Admin'), (2, 'Voter')], default=2, max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
