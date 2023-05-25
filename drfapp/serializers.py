from .models import Departments, Dept_emp, Dept_manager, Employees, Salaries, Titles
from .paginations import LargeResultsSetPagination

from rest_framework import serializers

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'
        
class DeptEmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dept_emp
        fields = '__all__'   
                
class DeptManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Dept_manager
        fields = '__all__'      
        
class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
        pagination_class = LargeResultsSetPagination      

class SalariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salaries
        fields = '__all__'       
        
class TitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titles
        fields = '__all__'      