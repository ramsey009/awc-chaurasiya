# Generated by Django 3.2.5 on 2021-08-12 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awcapp', '0005_auto_20210811_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='gravidwomeninfo',
            name='dob',
            field=models.DateField(blank=True, max_length=8, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='childinfo',
            name='cast',
            field=models.CharField(blank=True, choices=[('General', 'General'), ('Medium', 'Medium'), ('Lower', 'Lower')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='childinfo',
            name='condition',
            field=models.CharField(blank=True, max_length=220, null=True, verbose_name='Condition'),
        ),
    ]
