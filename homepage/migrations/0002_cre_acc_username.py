# Generated by Django 4.2.3 on 2023-08-18 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cre_acc',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
