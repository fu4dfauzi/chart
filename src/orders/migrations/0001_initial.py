# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-12 06:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('variables', '0001_initial'),
        ('teacher', '0001_initial'),
        ('student', '0001_initial'),
        ('opening', '0001_initial'),
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutor_rating', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('grp_tuition', models.BooleanField(default=False)),
                ('years_of_exp', models.PositiveIntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(auto_now=True)),
                ('teacherorder', models.BooleanField(default=False)),
                ('studentorder', models.BooleanField(default=False)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Inactive', 'Inactive'), ('Messaged', 'Messaged'), ('Rejected', 'Rejected'), ('Application', 'Application'), ('Offer', 'Offer'), ('Job In Progress', 'Job In Progress'), ('Completed', 'Completed'), ('Canceled', 'Canceled'), ('Reviewed', 'Reviewed')], default='Inactive', max_length=30)),
                ('expertise', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='variables.Expertise_Type')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='variables.Level_Expertise')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='variables.Region')),
                ('omessage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messaging.Message')),
                ('oopening', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opening.Opening')),
                ('ostudent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
                ('oteacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Teacher')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='variables.Subject_Expertise')),
            ],
        ),
    ]
