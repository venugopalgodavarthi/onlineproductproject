# Generated by Django 4.0.1 on 2022-01-21 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clothcompany',
            fields=[
                ('ccomid', models.BigAutoField(primary_key=True, serialize=False)),
                ('ccomname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='clothtype',
            fields=[
                ('ctid', models.BigAutoField(primary_key=True, serialize=False)),
                ('ctname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='grocaryitems',
            fields=[
                ('gid', models.BigAutoField(primary_key=True, serialize=False)),
                ('gitem', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='mobilecompany',
            fields=[
                ('comyid', models.BigAutoField(primary_key=True, serialize=False)),
                ('comyname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='productitem',
            fields=[
                ('itemid', models.BigAutoField(primary_key=True, serialize=False)),
                ('itemname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='mobiledetail',
            fields=[
                ('mid', models.BigAutoField(primary_key=True, serialize=False)),
                ('mname', models.CharField(max_length=50)),
                ('mmodelno', models.CharField(max_length=15)),
                ('mdesc', models.TextField(max_length=500)),
                ('imei', models.BigIntegerField()),
                ('mprice', models.FloatField()),
                ('mdiscount', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.mobilecompany')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productitem')),
            ],
        ),
        migrations.CreateModel(
            name='grocarydetail',
            fields=[
                ('gid', models.BigAutoField(primary_key=True, serialize=False)),
                ('gname', models.CharField(max_length=50)),
                ('gdesc', models.TextField(max_length=500)),
                ('gprice', models.FloatField()),
                ('gdiscount', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('gcompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.mobilecompany')),
                ('gitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productitem')),
                ('groitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.grocaryitems')),
            ],
        ),
        migrations.CreateModel(
            name='clothdetail',
            fields=[
                ('cid', models.BigAutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=50)),
                ('cmodelno', models.CharField(max_length=15)),
                ('cdesc', models.TextField(max_length=500)),
                ('category', models.CharField(choices=[['Male', 'MALE'], ['Female', 'FEMALE'], ['kids', 'KIDS']], max_length=15)),
                ('cprice', models.FloatField()),
                ('cdiscount', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('size', models.CharField(choices=[['Small', 'SMALL'], ['Medium', 'MEDIUM'], ['Large', 'LARGE'], ['ExtraLarge', 'EXTRALARGE'], ['DoubleExtra Large', 'DOUBLEEXTRA LARGE']], max_length=25)),
                ('ccompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.mobilecompany')),
                ('citem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productitem')),
                ('ctype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.clothtype')),
            ],
        ),
    ]
