# Generated by Django 4.2.9 on 2024-02-19 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=50)),
                ('descripcion_categoria', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=20, unique=True)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=255)),
                ('gmail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=20)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=255)),
                ('gmail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_producto', models.CharField(max_length=50)),
                ('nombre_producto', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=0, max_digits=10)),
                ('cantidad', models.PositiveIntegerField(null=True)),
                ('fecha_expiracion', models.DateField(blank=True, null=True)),
                ('fecha_recibida', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.FloatField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('hora', models.DateTimeField(auto_now_add=True)),
                ('metodo_pago', models.CharField(choices=[('debito', 'debito'), ('efectivo', 'efectivo'), ('tarjeta de credito', 'tarjeta de credito'), ('psi', 'psi'), ('nequi', 'nequi')], max_length=50)),
                ('total', models.FloatField()),
                ('id_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.empleados')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.productos')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_stock', models.IntegerField()),
                ('fecha_revision', models.CharField(max_length=100)),
                ('fecha_reposicion', models.CharField(max_length=100)),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.productos')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomproducto', models.IntegerField(max_length=100)),
                ('precio', models.CharField(max_length=100)),
                ('cantidad', models.CharField(max_length=100)),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.productos')),
            ],
        ),
    ]
