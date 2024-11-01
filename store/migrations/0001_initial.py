# Generated by Django 5.1.2 on 2024-10-28 11:48

import django.db.models.deletion
import store.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=15, null=True)),
                ('added_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomeMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_service_phone', models.CharField(max_length=15, null=True)),
                ('main_message1', models.CharField(max_length=15, null=True)),
                ('main_message1_description', models.TextField(max_length=100, null=True)),
                ('main_message2', models.CharField(max_length=15, null=True)),
                ('main_message2_description', models.TextField(max_length=100, null=True)),
                ('main_message3', models.CharField(max_length=15, null=True)),
                ('main_message3_description', models.TextField(max_length=100, null=True)),
                ('show_offer_messages', models.BooleanField(choices=[(True, 'Show'), (False, 'Hide')], default=True, null=True)),
                ('offer_message1', models.CharField(max_length=15, null=True)),
                ('offer_message1_description', models.CharField(max_length=15, null=True)),
                ('offer_message2', models.CharField(max_length=15, null=True)),
                ('offer_message2_description', models.CharField(max_length=15, null=True)),
                ('offer_message3', models.CharField(max_length=15, null=True)),
                ('offer_message3_description', models.CharField(max_length=15, null=True)),
                ('offer_message4', models.CharField(max_length=15, null=True)),
                ('offer_message4_description', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=15, null=True)),
                ('added_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
                ('bio', models.TextField(default='No Descrition.', max_length=300, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.CharField(choices=[('Formal Suits', 'Formal Suits'), ('Business Casual Suits', 'Business Casual Suits'), ('Lounge Suits', 'Lounge Suits'), ('Tuxedos', 'Tuxedos')], max_length=50, null=True)),
                ('image', models.ImageField(default='default_photos/default_prodct.jpg', upload_to='product/%Y%b%d')),
                ('published_at', models.DateField(auto_now=True)),
                ('rate', models.IntegerField(default=0, null=True)),
                ('colors', models.ManyToManyField(to='store.colors')),
                ('sizes', models.ManyToManyField(to='store.sizes')),
                ('tags', models.ManyToManyField(to='store.tags')),
            ],
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now=True)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.cart')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.products')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=14, null=True)),
                ('bio', models.TextField(max_length=150, null=True)),
                ('phone', models.CharField(max_length=14, null=True)),
                ('Country', models.CharField(blank=True, default='Unknown', max_length=40, null=True)),
                ('City', models.CharField(blank=True, default='Unknown', max_length=40, null=True)),
                ('image', models.ImageField(default='default_photos/default_user.png', upload_to=store.models.user_directory_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
