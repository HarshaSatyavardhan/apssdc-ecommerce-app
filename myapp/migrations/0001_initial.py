# Generated by Django 2.1.5 on 2020-05-27 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BilingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(blank=True, choices=[('Home', 'Home'), ('Office', 'Office'), ('Other', 'Other')], max_length=10, null=True)),
                ('street_address', models.CharField(max_length=255)),
                ('apartment_address', models.CharField(max_length=255)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('zipcode', models.CharField(max_length=10)),
                ('default_address', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='CheckZipcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DiscountCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promo_code', models.CharField(max_length=20)),
                ('amount', models.FloatField()),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('label', models.CharField(blank=True, choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], max_length=1, null=True)),
                ('label_name', models.CharField(blank=True, choices=[('N', 'NEW'), ('S', 'SALE'), ('D', 'DISCOUNT'), ('O', 'OFFER')], max_length=1, null=True)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('list_on_frontpage', models.BooleanField(blank=True, default=False, null=True)),
                ('category', models.ManyToManyField(to='myapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.BilingAddress')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.DiscountCode')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_charge_id', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=120, null=True)),
                ('lastname', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.EmailField(blank=True, max_length=120, null=True)),
                ('profile_picture', models.ImageField(default='default_user.png', upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wishlisted', models.BooleanField(default=False)),
                ('wishlisted_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='WishlistedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wishlisted', models.BooleanField(default=False)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='wishlish',
            name='item',
            field=models.ManyToManyField(to='myapp.WishlistedItem'),
        ),
        migrations.AddField(
            model_name='wishlish',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='myapp.OrderItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.Payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]