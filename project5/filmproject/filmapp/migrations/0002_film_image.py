# Generated by Django 4.1.5 on 2023-01-07 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='image',
            field=models.ImageField(default='asdf', upload_to='Gallery'),
            preserve_default=False,
        ),
    ]
