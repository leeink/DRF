from django.db import models

# Create your models here.
class Departments(models.Model):
    dept_no = models.CharField(primary_key=True,max_length=4)
    dept_name = models.CharField(max_length=40,unique=True)
    
    class Meta:
        db_table = 'departments'
    
class Employees(models.Model):
    emp_no = models.IntegerField(primary_key=True)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1)
    hire_date = models.DateField()
    
    class Meta:
        db_table = 'employees'
    
class Dept_emp(models.Model):
    emp_no = models.OneToOneField(Employees,on_delete=models.CASCADE, to_field='emp_no',
                               related_name='dept_emp',primary_key=True,db_column='emp_no',)
    dept_no = models.ForeignKey(Departments,on_delete=models.CASCADE,to_field='dept_no',
                                related_name='dept_emp',db_column='dept_no')
    from_date = models.DateField()
    to_date = models.DateField()
    
    class Meta:
        unique_together = (('emp_no','dept_no'))
        db_table = 'dept_emp'
    
class Dept_manager(models.Model):
    emp_no = models.OneToOneField(Employees,on_delete=models.CASCADE, to_field='emp_no',
                               related_name='dept_manager',primary_key=True,db_column='emp_no',)
    dept_no = models.ForeignKey(Departments,on_delete=models.CASCADE,to_field='dept_no',
                                related_name='dept_manager',db_column='dept_no')
    from_date = models.DateField()
    to_date = models.DateField()
    
    class Meta:
        unique_together = (('emp_no','dept_no'))
        db_table = 'dept_manager'
    
class Salaries(models.Model):
    emp_no = models.OneToOneField(Employees, on_delete=models.CASCADE,to_field='emp_no',
                                related_name='salaries', db_column='emp_no')
    salary = models.IntegerField()
    from_date = models.DateField(primary_key=True)
    to_date = models.DateField()
    
    class Meta:
        db_table = 'salaries'
        
class Titles(models.Model):
    emp_no = models.OneToOneField(Employees, on_delete=models.CASCADE, to_field='emp_no',
                               related_name='title',primary_key=True,db_column='emp_no')
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    
    class Meta:
        db_table = 'titles'
        unique_together = (('emp_no','title', 'from_date'))