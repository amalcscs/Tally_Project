# Generated by Django 4.0.2 on 2022-08-22 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_currency_alt'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=100, null=True)),
                ('start_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='stock_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('alias', models.CharField(max_length=100, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('rateper', models.IntegerField(null=True)),
                ('value', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stockcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='StockGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grp_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='voucherlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(max_length=100, null=True)),
                ('vouch_type', models.CharField(max_length=100, null=True)),
                ('date', models.DateField()),
                ('quantity', models.IntegerField()),
                ('rateper', models.IntegerField(null=True)),
                ('value', models.IntegerField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.stockcategory')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.stockgroup')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.stock_item')),
            ],
        ),
        migrations.AddField(
            model_name='stock_item',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.stockcategory'),
        ),
        migrations.AddField(
            model_name='stock_item',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.stockgroup'),
        ),
        migrations.CreateModel(
            name='CreateStockGrp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=100)),
                ('under', models.CharField(max_length=100, null=True)),
                ('quantities', models.CharField(max_length=100, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.stockgroup')),
            ],
        ),
        migrations.CreateModel(
            name='CreateStockCateg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=100)),
                ('under', models.CharField(max_length=50)),
                ('quantities', models.CharField(max_length=100, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.stockcategory')),
            ],
        ),
    ]
