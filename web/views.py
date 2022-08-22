import imp
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import CompaniaSerializer
from .models import Compania
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
import json
# Create your views here.
def index(request):
    return HttpResponse("<h2>web</h2>")


class CompaniaList(APIView):
    
    def get(self, request, format=None):
       companias = Compania.objects.all()
       serializer = CompaniaSerializer(companias,many=True)
       #return JsonResponse(serializer.data,safe=False)
       return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CompaniaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""     companias = Compania.objects.all()
    serializer = CompaniaSerializer(companias,many=True)
    return JsonResponse(serializer.data,safe=False) """

class CampaniaDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Compania.objects.get(pk=pk)
        except Compania.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        compania = self.get_object(pk)
        serializer = CompaniaSerializer(compania)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        compania = self.get_object(pk)
        serializer = CompaniaSerializer(compania, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        compania = self.get_object(pk)
        compania.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)