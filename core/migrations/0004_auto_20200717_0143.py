# Generated by Django 3.0.8 on 2020-07-16 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200717_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], default='S', max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
    ]
