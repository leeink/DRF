from .models import Departments, Dept_emp, Dept_manager, Employees, Salaries, Titles
from .serializers import DepartmentsSerializer, DeptEmpSerializer,DeptManagerSerializer, EmployeesSerializer, SalariesSerializer, TitlesSerializer
from .paginations import LargeResultsSetPagination

from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [DjangoFilterBackend]
    pagination_class = LargeResultsSetPagination

class DeptEmpViewSet(viewsets.ModelViewSet):
    queryset = Dept_emp.objects.all()
    serializer_class = DeptEmpSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [DjangoFilterBackend]
    pagination_class = LargeResultsSetPagination
    
class DeptManagerViewSet(viewsets.ModelViewSet):
    queryset = Dept_manager.objects.all()
    serializer_class = DeptManagerSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [DjangoFilterBackend]
    pagination_class = LargeResultsSetPagination
    
class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [DjangoFilterBackend]
    pagination_class = LargeResultsSetPagination
class SalariesViewSet(viewsets.ModelViewSet):
    queryset = Salaries.objects.all()
    serializer_class = SalariesSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [DjangoFilterBackend]
    pagination_class = LargeResultsSetPagination
    
class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [DjangoFilterBackend]
    pagination_class = LargeResultsSetPagination