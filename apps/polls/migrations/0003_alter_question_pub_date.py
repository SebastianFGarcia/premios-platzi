# Generated by Django 4.0.3 on 2022-03-29 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_choices_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha Publicación'),
        ),
    ]