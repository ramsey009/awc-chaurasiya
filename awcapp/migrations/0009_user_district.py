# Generated by Django 3.2.5 on 2021-09-04 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awcapp', '0008_teenagegirl_mobile_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='awcapp.district'),
        ),
    ]
