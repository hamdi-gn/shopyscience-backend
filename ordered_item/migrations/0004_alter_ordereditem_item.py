# Generated by Django 4.0.6 on 2022-07-31 07:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ordered_item', '0003_alter_ordereditem_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordereditem',
            name='Item',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
