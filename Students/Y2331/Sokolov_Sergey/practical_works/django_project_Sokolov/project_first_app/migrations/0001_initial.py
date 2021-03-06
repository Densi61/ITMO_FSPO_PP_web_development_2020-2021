# Generated by Django 3.1.7 on 2021-03-03 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_number', models.CharField(max_length=15)),
                ('brand', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('colour', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CarOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Own',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.car')),
                ('id_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.carowner')),
            ],
        ),
        migrations.CreateModel(
            name='DriverLicense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_license', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('id_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.carowner')),
            ],
        ),
    ]
