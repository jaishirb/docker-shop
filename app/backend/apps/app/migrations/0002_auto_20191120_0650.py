# Generated by Django 2.2 on 2019-11-20 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariotienda',
            name='tienda',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.Tienda'),
        ),
    ]