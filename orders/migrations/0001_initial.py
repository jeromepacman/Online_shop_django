# Generated by Django 3.1.3 on 2020-11-14 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0007_auto_20201114_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='prénom')),
                ('last_name', models.CharField(max_length=50, verbose_name='nom')),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=250, verbose_name='adresse')),
                ('postal_code', models.CharField(max_length=5, verbose_name='code postal')),
                ('city', models.CharField(max_length=100, verbose_name='ville')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='date de mise à jour')),
                ('paid', models.BooleanField(default=False, verbose_name='validation')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='prix')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='quantité')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order', verbose_name='historique')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.product', verbose_name='produit')),
            ],
        ),
    ]
