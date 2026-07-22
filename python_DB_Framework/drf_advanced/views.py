from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from employee_api.models import Employee
from employee_api.serializers import EmployeeSerializer

class AdvancedEmployeeViewSet(viewsets.ModelViewSet):
    """
    Advanced ViewSet for Employee that supports pagination, filtering, searching, and ordering.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    # Define which backends to use for filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # 1. DjangoFilterBackend: Exact match on department, range match on salary
    filterset_fields = {
        'department': ['exact'],
        'salary': ['gte', 'lte'],
    }
    
    # 2. SearchFilter: Text search across name
    search_fields = ['name']
    
    # 3. OrderingFilter: Sorting based on salary or name
    ordering_fields = ['salary', 'name']
