# Generated by Django 4.1.7 on 2023-02-17 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('dept_no', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('birth_date', models.DateField()),
                ('first_name', models.CharField(max_length=14)),
                ('last_name', models.CharField(max_length=16)),
                ('gender', models.CharField(max_length=1)),
                ('hire_date', models.DateField()),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='Salaries',
            fields=[
                ('salary', models.IntegerField()),
                ('from_date', models.DateField(primary_key=True, serialize=False)),
                ('to_date', models.DateField()),
                ('emp_no', models.OneToOneField(db_column='emp_no', on_delete=django.db.models.deletion.CASCADE, related_name='salaries', to='drfapp.employees')),
            ],
            options={
                'db_table': 'salaries',
            },
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('emp_no', models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='title', serialize=False, to='drfapp.employees')),
                ('title', models.CharField(max_length=50)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
            options={
                'db_table': 'titles',
                'unique_together': {('emp_no', 'title', 'from_date')},
            },
        ),
        migrations.CreateModel(
            name='Dept_manager',
            fields=[
                ('emp_no', models.OneToOneField(db_column='emp_no', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='dept_manager', serialize=False, to='drfapp.employees')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('dept_no', models.ForeignKey(db_column='dept_no', on_delete=django.db.models.deletion.CASCADE, related_name='dept_manager', to='drfapp.departments')),
            ],
            options={
                'db_table': 'dept_manager',
                'unique_together': {('emp_no', 'dept_no')},
            },
        ),
        migrations.CreateModel(
            name='Dept_emp',
            fields=[
                ('emp_no', models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='dept_emp', serialize=False, to='drfapp.employees')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('dept_no', models.ForeignKey(db_column='dept_no', on_delete=django.db.models.deletion.CASCADE, related_name='dept_emp', to='drfapp.departments')),
            ],
            options={
                'db_table': 'dept_emp',
                'unique_together': {('emp_no', 'dept_no')},
            },
        ),
    ]
