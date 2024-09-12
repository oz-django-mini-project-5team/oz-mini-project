# Generated by Django 5.1.1 on 2024-09-11 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_account_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="balance",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=14),
        ),
    ]
