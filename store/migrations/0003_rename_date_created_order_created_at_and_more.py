# Generated by Django 5.0.12 on 2025-02-16 14:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_date_order_date_created_remove_cookie_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='cookie',
            name='description',
        ),
        migrations.AddField(
            model_name='cookie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cookie_images/'),
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(default='000-000-0000', max_length=20),
        ),
        migrations.AlterField(
            model_name='cookie',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='store.order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
