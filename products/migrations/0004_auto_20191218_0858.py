# Generated by Django 3.0 on 2019-12-18 08:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20191218_0835'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendor',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='vendor',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Name'),
        ),
    ]
