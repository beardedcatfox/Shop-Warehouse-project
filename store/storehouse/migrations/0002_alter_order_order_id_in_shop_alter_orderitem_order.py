# Generated by Django 4.1.7 on 2023-04-08 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storehouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id_in_shop',
            field=models.IntegerField(unique=True, verbose_name='Order id in shop'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storehouse.order', to_field='order_id_in_shop'),
        ),
    ]
