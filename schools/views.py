from django.http import JsonResponse, HttpResponse
from .models import School
from .api.serializers import SchoolSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def api(request):
    return HttpResponse("Hello, You're at the API Documentation.")

@api_view(['GET','POST'])
def school_list(request, format=None):
  if request.method == 'GET':
    schools = School.objects.all()
    serializer = SchoolSerializer(schools, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  if request.method == 'POST':
    serializer = SchoolSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def school_detail (request, id, format=None):
  try: 
    school = School.objects.get(pk=id)
  except School.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = SchoolSerializer(school)
    return Response(serializer.data, status=status.HTTP_200_OK)

  elif request.method == 'PUT':
    serializer = SchoolSerializer(school, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    school.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
 
