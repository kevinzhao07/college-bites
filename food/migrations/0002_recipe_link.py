# Generated by Django 3.0.7 on 2020-07-31 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='link',
            field=models.CharField(default='s', max_length=280),
            preserve_default=False,
        ),
    ]