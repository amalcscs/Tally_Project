# Generated by Django 4.0.2 on 2022-08-23 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_cost_centre_company_currencyalteration_company_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cost_center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=255)),
                ('cost_alias', models.CharField(max_length=255)),
                ('under', models.CharField(max_length=255)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies')),
            ],
        ),
    ]
