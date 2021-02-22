from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from .models import Product

#class based views

class ProductList(APIView):
    """
    List all products, create, update & delete product 
    """
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, format = None):
        key = request.query_params
        if bool(key):
            product = self.get_object(key['pk'])
            serializer = ProductSerializer(product)
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many = True)        
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def post(self, request, format = None):
        
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def put(self, request, pk, format = None):

    #     serializer = ProductSerializer(self.get_object(pk), data= request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"msg" : "product is updated successfully"}, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)
    
    def put(self, request, format = None):
        serializer = ProductSerializer(self.get_object(request.query_params['pk']), data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg" : "product is updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

    def delete(self, request, format = None):
        item = self.get_object(request.query_params['pk'])
        item.delete()
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)