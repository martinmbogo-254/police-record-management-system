# Generated by Django 4.1.3 on 2023-01-16 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrest',
            name='incidence',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='records.report'),
        ),
    ]