# Generated by Django 4.2.4 on 2023-09-11 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'admin'), (2, 'instructor'), (3, 'student')])),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('first_name', models.CharField(max_length=25)),
                ('surname', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=20)),
                ('dob', models.DateField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_courier', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
                ('otp', models.CharField(max_length=6)),
                ('verified', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
