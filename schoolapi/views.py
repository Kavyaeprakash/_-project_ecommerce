
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serialiser import Student_Serializer
from django.http import JsonResponse

# Create your views here.

@api_view(['POST'])
def add_student(request):
    serialized_data = Student_Serializer(data = request.data)
    msg = ''
    if serialized_data.is_valid():
        serialized_data.save()
        msg = 'Data added successfully'
        return JsonResponse({'msg':msg})
    else:
        msg = 'Invalid details'
        return JsonResponse({'msg':msg})
    
@api_view(['GET'])
def view_student(request):
    students = Student.objects.all()
    serialized_data = Student_Serializer(students,many = True)
    return JsonResponse(serialized_data.data,safe = False)

@api_view(['PUT'])
def update_student(request,student_id):
    student = Student.objects.get(id = student_id)
    serialized_data = Student_Serializer(student,data = request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({'msg':'updated successfully'})
    else:
        return JsonResponse({'msg':'invalid data'})
    

@api_view(['DELETE'])
def delete_student(request,student_id):
    student = Student.objects.get(id = student_id)
    student.delete()
    return JsonResponse({'msg':'deleted successfully'})

@api_view(['GET'])
def index(request):
    msg = 'congratulations'
    return Response(msg)


