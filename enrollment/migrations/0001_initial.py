# Generated by Django 4.2.4 on 2023-09-11 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enrolled', models.DateTimeField(auto_now_add=True)),
                ('progress', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('active', 'Active'), ('completed', 'Completed'), ('dropped', 'Dropped')], default='active', max_length=10)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('grade', models.FloatField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
    ]
