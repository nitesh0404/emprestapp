from django.db import models

# Create your models here.
class Employee_Info(models.Model):
    emp_name = models.CharField('Employee Name', max_length=120)
    emp_join_date = models.DateTimeField('Join Date')
    emp_address = models.CharField(max_length=120)
    emp_dept = models.CharField(max_length=60)
