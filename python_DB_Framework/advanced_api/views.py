from rest_framework import viewsets
from employee_api.models import Employee
from employee_api.serializers import EmployeeSerializer
from .permissions import IsAdminUserOrReadOnly

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Employee.
    
    # Task 4 Verification:
    # Basic Authentication is enforced globally. Navigating to the endpoint anonymously yields a 403 Forbidden.
    # A superuser (admin/admin123) was created via shell. Supplying these credentials successfully authenticates the request and grants access to the API view.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    # Custom permission: Admin can edit/delete, authenticated users can read.
    # Note: Global settings already require IsAuthenticated.
    permission_classes = [IsAdminUserOrReadOnly]
