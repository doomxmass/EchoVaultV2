# Generated by Django 5.1.2 on 2024-10-31 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_blacklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default='default_photos/default_product.jpg', upload_to='product/%Y%b%d'),
        ),
    ]
