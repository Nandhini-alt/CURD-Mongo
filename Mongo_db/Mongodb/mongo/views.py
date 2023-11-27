from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentSerializer
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404

class StudentView(APIView):
    def get(self, request, id=None):
        if id is not None:
            try:
                student = Students.objects.get(id=id)
                serializer = StudentSerializer(student)
                return Response({'Students': serializer.data}, status=200)
            except Students.DoesNotExist:
                raise NotFound("Student does not exist")
        else:
            student = Students.objects.all()
            serializers = StudentSerializer(student, many=True)
            return Response({'students': serializers.data}, status=200)
      
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'data':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, id=None):
        if id is not None:
            try:
                student = Students.objects.get(id=id)
                serializer = StudentSerializer(student, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': 'student detail updated successfully'}, status=200)
                return Response(serializer.errors, status=400)
            except Students.DoesNotExist:
                raise NotFound("Student does not exist")
        else:
            return Response({'error': 'Please provide an ID for Updating an student'}, status=400)
    
    def delete(self, request, id=None):
        result = get_object_or_404(Students, id=id)
        result.delete()
        return Response({'message':'Record Deleted successfully'})
