# Generated by Django 3.1.3 on 2020-11-13 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20201113_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, verbose_name='disponibilité'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='création'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=150, verbose_name='nom'),
        ),
    ]