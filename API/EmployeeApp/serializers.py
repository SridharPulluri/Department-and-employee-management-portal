from rest_framework import serializers
from EmployeeApp.models import Departments, Employees

class DepartmentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'

class EmployeeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName']

