# Generated by Django 4.1.2 on 2022-10-30 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_alter_voter_reg_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voter',
            name='reg_no',
        ),
        migrations.AlterField(
            model_name='voter',
            name='otp',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='phone',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
