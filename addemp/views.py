from django.shortcuts import render
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .models import Employee_Info
from .serializer import EmployeeSerializer
# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = Employee_Info.objects.all()
    serializer_class = EmployeeSerializer
# Create your views here.
