# Generated by Django 2.2 on 2019-11-20 06:44

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tienda',
                'verbose_name_plural': 'Tiendas',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Tienda')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.CreateModel(
            name='UsuarioTienda',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Tienda')),
            ],
            options={
                'verbose_name': 'Usuario Tienda',
                'verbose_name_plural': 'Usuarios Tiendas',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ProductoVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_unidad', models.PositiveIntegerField()),
                ('cantidad', models.PositiveIntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Producto')),
                ('tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Tienda')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='app.Venta')),
            ],
            options={
                'verbose_name': 'Producto Venta',
                'verbose_name_plural': 'Productos Ventas',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='tienda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Tienda'),
        ),
    ]
