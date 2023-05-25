from rest_framework import routers
from .views import DepartmentsViewSet, DeptEmpViewSet, DeptManagerViewSet, EmployeesViewSet, SalariesViewSet, TitlesViewSet

router = routers.DefaultRouter()

router.register(r'^departments',DepartmentsViewSet)
router.register(r'^deptemp',DeptEmpViewSet)
router.register(r'^deptmanager',DeptManagerViewSet)
router.register(r'^employees',EmployeesViewSet)
router.register(r'^salaries',SalariesViewSet)
router.register(r'^titles',TitlesViewSet)

urlpatterns = router.urls