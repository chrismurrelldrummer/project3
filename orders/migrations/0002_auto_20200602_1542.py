# Generated by Django 2.0.3 on 2020-06-02 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('time_placed', models.TimeField(auto_now_add=True)),
                ('cost', models.DecimalField(decimal_places=2, default='00.00', max_digits=6)),
                ('active', models.CharField(default='Y', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Platter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(max_length=64)),
                ('size', models.CharField(max_length=5)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(max_length=64)),
                ('size', models.CharField(max_length=5)),
                ('extras', models.ManyToManyField(related_name='subs', to='orders.Extras')),
            ],
        ),
        migrations.RemoveField(
            model_name='pizitem',
            name='top1',
        ),
        migrations.RemoveField(
            model_name='pizitem',
            name='top2',
        ),
        migrations.RemoveField(
            model_name='pizitem',
            name='top3',
        ),
        migrations.RenameField(
            model_name='toppings',
            old_name='name',
            new_name='typ',
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(related_name='pizzas', to='orders.Toppings'),
        ),
        migrations.DeleteModel(
            name='PizItem',
        ),
        migrations.AddField(
            model_name='orders',
            name='pastaItems',
            field=models.ManyToManyField(related_name='pastaItems', to='orders.Pasta'),
        ),
        migrations.AddField(
            model_name='orders',
            name='pizItems',
            field=models.ManyToManyField(related_name='pizItems', to='orders.Pizza'),
        ),
        migrations.AddField(
            model_name='orders',
            name='platItems',
            field=models.ManyToManyField(related_name='platItems', to='orders.Platter'),
        ),
        migrations.AddField(
            model_name='orders',
            name='saladItems',
            field=models.ManyToManyField(related_name='saladItems', to='orders.Salad'),
        ),
        migrations.AddField(
            model_name='orders',
            name='subItems',
            field=models.ManyToManyField(related_name='subItems', to='orders.Sub'),
        ),
        migrations.AddField(
            model_name='orders',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
    ]