# Generated by Django 3.2.8 on 2021-12-01 20:42

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import psqlextra.backend.migrations.operations.add_default_partition
import psqlextra.backend.migrations.operations.create_partitioned_model
import psqlextra.manager.manager
import psqlextra.models.partitioned
import psqlextra.types


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('platform', models.SmallIntegerField(choices=[(1, 'Django'), (2, 'Naver'), (3, 'Google'), (4, 'Kakao')], default=1)),
                ('gender', models.CharField(choices=[('M', '남성'), ('F', '여성')], max_length=1, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('is_manager', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        psqlextra.backend.migrations.operations.create_partitioned_model.PostgresCreatePartitionedModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('status', models.IntegerField(choices=[(0, '미정'), (1, '정상 출근'), (2, '조퇴'), (3, '결근'), (4, '연차')], default=0)),
                ('is_confirmed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            partitioning_options={
                'method': psqlextra.types.PostgresPartitioningMethod['RANGE'],
                'key': ['date'],
            },
            bases=(psqlextra.models.partitioned.PostgresPartitionedModel,),
            managers=[
                ('objects', psqlextra.manager.manager.PostgresManager()),
            ],
        ),
        psqlextra.backend.migrations.operations.add_default_partition.PostgresAddDefaultPartition(
            model_name='Attendance',
            name='default',
        ),
        migrations.CreateModel(
            name='CouponHold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(auto_now_add=True)),
                ('used_date', models.DateField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_date', models.DateField()),
                ('salary', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeEvaluationByEmployer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluate1', models.IntegerField()),
                ('evaluate2', models.IntegerField()),
                ('evaluate3', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeEvaluationByUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluate1', models.IntegerField()),
                ('evaluate2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('benefits', models.JSONField()),
            ],
        ),
        psqlextra.backend.migrations.operations.create_partitioned_model.PostgresCreatePartitionedModel(
            name='Mileage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.BigIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('point', models.IntegerField()),
                ('content', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            partitioning_options={
                'method': psqlextra.types.PostgresPartitioningMethod['RANGE'],
                'key': ['created'],
            },
            bases=(psqlextra.models.partitioned.PostgresPartitionedModel,),
            managers=[
                ('objects', psqlextra.manager.manager.PostgresManager()),
            ],
        ),
        psqlextra.backend.migrations.operations.add_default_partition.PostgresAddDefaultPartition(
            model_name='Mileage',
            name='default',
        ),
        migrations.CreateModel(
            name='NonCouponHold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('used_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/%Y/%m/')),
            ],
        ),
    ]
