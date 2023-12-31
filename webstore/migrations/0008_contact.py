# Generated by Django 4.2 on 2023-05-06 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstore', '0007_alter_category_id_alter_customer_id_alter_order_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]
