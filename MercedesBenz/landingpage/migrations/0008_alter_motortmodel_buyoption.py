# Generated by Django 4.1.3 on 2022-12-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0007_alter_motortmodel_buyoption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motortmodel',
            name='BuyOption',
            field=models.IntegerField(choices=[(1, 'پلنگ'), (2, 'گربه')], default=1),
        ),
    ]