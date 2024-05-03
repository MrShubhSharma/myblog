# Generated by Django 4.0.6 on 2022-07-22 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0011_alter_invoiceitem_tax_rates_and_more'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djstripe.customer'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djstripe.subscription'),
        ),
    ]