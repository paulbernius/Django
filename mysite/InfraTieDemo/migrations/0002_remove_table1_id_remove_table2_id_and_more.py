# Generated by Django 4.0.4 on 2022-05-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfraTieDemo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table1',
            name='id',
        ),
        migrations.RemoveField(
            model_name='table2',
            name='id',
        ),
        migrations.AlterField(
            model_name='table1',
            name='InspectionID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='table2',
            name='ConditionID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
