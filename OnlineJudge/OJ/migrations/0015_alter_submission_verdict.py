# Generated by Django 4.0 on 2022-07-12 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OJ', '0014_remove_problem_sample_input_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='verdict',
            field=models.CharField(max_length=100),
        ),
    ]