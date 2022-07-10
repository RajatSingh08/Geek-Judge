# Generated by Django 4.0 on 2022-07-09 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100000)),
                ('difficulty', models.CharField(max_length=10)),
                ('solved_status', models.CharField(max_length=10)),
                ('score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_score', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.CharField(max_length=1000000)),
                ('output', models.CharField(max_length=1000000)),
                ('problem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OJ.problem')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField()),
                ('user_code', models.CharField(max_length=100000)),
                ('verdict', models.CharField(max_length=100)),
                ('problem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OJ.problem')),
            ],
        ),
    ]