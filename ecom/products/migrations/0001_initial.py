# Generated by Django 3.1.7 on 2021-02-21 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_type', models.CharField(choices=[('PR', 'Premium'), ('GD', 'Gold'), ('RG', 'Regular')], default='RG', max_length=2)),
                ('product_category', models.CharField(choices=[('M', 'Men Clothing'), ('W', 'Women Clothing'), ('C', 'Children Clothing')], default='M', max_length=2)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('details', models.TextField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('discount', models.FloatField(max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
