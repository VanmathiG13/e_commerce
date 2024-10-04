# Generated by Django 4.2.16 on 2024-10-02 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('image_url', models.URLField()),
                ('mrp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discounted_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_count', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='main.category')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
