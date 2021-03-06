# Generated by Django 3.2.5 on 2021-09-06 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awcapp', '0011_auto_20210906_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='deathinfo',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='awcapp.district'),
        ),
        migrations.AddField(
            model_name='gravidwomeninfo',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='awcapp.district'),
        ),
        migrations.AddField(
            model_name='postpartummother',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='awcapp.district'),
        ),
        migrations.AddField(
            model_name='teenagegirl',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='awcapp.district'),
        ),
    ]
