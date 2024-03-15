from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        department_serializer = DepartmentSerializer(departments, many = True)
        return JsonResponse(department_serializer.data, safe = False)
    
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data = department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully", safe= False)
        return JsonResponse("Failed to Add sridhar!!!", safe= False)
    
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId = department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(department, data = department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated", safe = False)
        return JsonResponse("Failed to update", safe= False)
    
    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId = id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    # elif request.method == 'DELETE':                                      error handling
    #     try:
    #         department = Departments.objects.get(DepartmentId=id)
    #         department.delete()
    #         return JsonResponse("Deleted Successfully", safe=False)
    #     except Departments.DoesNotExist:
    #         return JsonResponse("Department not found", safe=False, status=404)


# Employee CRUD
@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employee_serializer = EmployeeSerializer(employees, many = True)
        return JsonResponse(employee_serializer.data, safe = False)
    
    elif request.method == 'POST':
        try:
            employee_data = JSONParser().parse(request)
            employee_serializer = EmployeeSerializer(data = employee_data)
            if employee_serializer.is_valid():
                employee_serializer.save()
                return JsonResponse("Added Successfully", safe= False)
            return JsonResponse("Failed to emp Add", safe= False)
        except:
            return JsonResponse("Unable to add Employee", safe=False, status=404)
    
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId = employee_data['EmployeeId'])
        employee_serializer = EmployeeSerializer(employee, data = employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated", safe = False)
        return JsonResponse("Failed to update", safe= False)
    
    # elif request.method == 'DELETE':
    #     employee = Employees.objects.get(EmployeeId=id)
    #     employee.delete()
    #     return JsonResponse("Deleted Successfully", safe=False)
    elif request.method == 'DELETE':
        try:
            employee = Employees.objects.get(EmployeeId=id)
            employee.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except Employees.DoesNotExist:
            return JsonResponse("Employee not found", safe=False, status=404)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)

