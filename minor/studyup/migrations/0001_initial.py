# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-17 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=500)),
                ('answer_image', models.ImageField(blank=True, null=True, upload_to='pics/')),
                ('time_stamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=100)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=500)),
                ('question_image', models.ImageField(blank=True, null=True, upload_to='pics/')),
                ('time_stamp', models.DateField(auto_now_add=True)),
                ('polls', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.PositiveSmallIntegerField()),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('contact', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('category', models.CharField(choices=[('S', 'Student'), ('T', 'Teacher'), ('G', 'Guardian')], max_length=1)),
                ('qualification', models.CharField(choices=[('a', 'Secondary'), ('b', 'Senior Secondary'), ('c', 'Undergraduate'), ('d', 'Postgraduate')], max_length=1)),
                ('area', models.CharField(choices=[('CS', 'Computer Science'), ('Maths', 'Mathematics'), ('Phy', 'Physics'), ('Chem', 'Chemistry'), ('Bio', 'Biology')], max_length=5)),
                ('current_institution', models.CharField(max_length=30)),
                ('about', models.TextField()),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyup.User'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyup.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyup.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyup.User'),
        ),
    ]
