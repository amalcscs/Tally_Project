# Generated by Django 4.0.4 on 2022-08-22 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_gst_app_from_alter_gst_applicable_form_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gst_taxability',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
    ]
