# Generated by Django 4.1.3 on 2022-12-02 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0006_remove_motortmodel_motorbtntitle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motortmodel',
            name='BuyOption',
            field=models.PositiveSmallIntegerField(choices=[('Sold', 'فروشی'), ('Rent', 'اجاره ایی')], default=1),
        ),
    ]
