# Generated by Django 4.1.3 on 2022-12-22 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0003_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='total_cost',
            field=models.FloatField(null=True, verbose_name='coût total'),
        ),
    ]