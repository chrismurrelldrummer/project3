# Generated by Django 3.0.7 on 2020-06-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_delete_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='pastaorder',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='pizorder',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='lgPrice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='smPrice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='platter',
            name='lgPrice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='platter',
            name='smPrice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='platterorder',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='saladorder',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='sub',
            name='lgPrice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='sub',
            name='smPrice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='suborder',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
    ]