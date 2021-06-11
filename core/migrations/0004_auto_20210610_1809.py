# Generated by Django 3.2.3 on 2021-06-10 21:09

from django.db import migrations, models
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210610_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='nationality',
            field=models.CharField(max_length=50, verbose_name='Nacionalidade'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='state',
            field=localflavor.br.models.BRStateField(max_length=2, verbose_name='Estado'),
        ),
    ]