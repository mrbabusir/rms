from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import CategorySerializer
from rest_framework.serializers import ValidationError
# Create your views here.
@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "deatil": "NEw Category Created",	
            })
@api_view(['GET', 'DELETE','PUT'])
def category_detail(request, id):
    if request.method == 'GET':
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "detail": "Category Updated",
        })
    elif request.method == 'DELETE':
        category = Category.objects.get(id=id)
        # Check if there are any food items associated with this category
        count = Orderitems.objects.filter(food__category = category).count()
        # If there are food items, do not allow deletion
        if count > 0:
            return Response({
                    "detail": "Cannot delete category with existing food items",
                })     
        
        category.delete()
        return Response({
            "detail": "Category Deleted",
        })