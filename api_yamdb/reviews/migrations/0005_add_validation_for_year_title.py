# Generated by Django 2.2.16 on 2022-09-12 08:08

import django.core.validators
from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_title_rename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Оценка должна быть от 1 до 10'), django.core.validators.MaxValueValidator(10, message='Оценка должна быть от 1 до 10')], verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(validators=[reviews.validators.validate_year], verbose_name='Год'),
        ),
    ]