# Generated by Django 3.2 on 2024-02-04 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20240203_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titles', to='reviews.category'),
        ),
    ]
