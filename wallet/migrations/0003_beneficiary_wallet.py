# Generated by Django 4.2 on 2023-04-09 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_alter_wallet_wallet_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiary',
            name='wallet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet'),
        ),
    ]