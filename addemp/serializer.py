from rest_framework.serializers import ModelSerializer
from .models import Employee_Info


class EmployeeSerializer(ModelSerializer):
        class Meta:
            model = Employee_Info
            fields = '__all__'