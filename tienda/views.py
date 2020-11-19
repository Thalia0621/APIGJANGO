from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import categories
from .serializers import categories_serializer
from .models import customers
from .serializers import customers_serializer
from .models import products
from .serializers import products_serializer
from .models import order
from .serializers import order_serializer
from .models import orderDetail
from .serializers import orderdetail_serializer
from rest_framework.permissions import IsAuthenticated

# ******Views Category****** 
@api_view(['GET', 'POST'])
#permission_classes = (IsAuthenticated,)
def categorieslist(request):
    #permission_classes = (IsAuthenticated,)
    """
    List all, or create a new register
    """
    if request.method == 'GET':
            categorias = categories.objects.all()
            serializer = categories_serializer(categorias, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = categories_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def detailcate(request, id):
    """
    Retrieve, update or delete a code categories.
    """
    try:
        categorias = categories.objects.get(id=id)
    except categorias.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = categories_serializer(categorias)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = categories_serializer(categorias, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        categorias.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

#****Customers****
@api_view(['GET', 'POST'])
def customerslist(request):
    """
    List all, or create a new register
    """
    if request.method == 'GET':
            custom = customers.objects.all()
            serializer = customers_serializer(custom, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = customers_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def customersdetail(request, id):
    """
    Retrieve, update or delete a code customers.
    """
    try:
        custom = customers.objects.get(id=id)
    except custom.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = customers_serializer(custom)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = customers_serializer(custom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        custom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#****Products****
@api_view(['GET', 'POST'])
def productslist(request):
    """
    List all, or create a new register
    """
    if request.method == 'GET':
            product = products.objects.all()
            serializer = products_serializer(product, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = products_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def productsdetail(request, id):
    """
    Retrieve, update or delete a code products.
    """
    try:
        product = products.objects.get(id=id)
    except product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = products_serializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = products_serializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#****Order****
@api_view(['GET', 'POST'])
def orderlist(request):
    """
    List all, or create a new register
    """
    if request.method == 'GET':
            orders = order.objects.all()
            serializer = order_serializer(orders, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = order_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def orderdetail(request, id):
    """
    Retrieve, update or delete a code order.
    """
    try:
        orders = order.objects.get(id=id)
    except orders.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = order_serializer(orders)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = order_serializer(orders, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        orders.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#****Order Detail****
@api_view(['GET', 'POST'])
def orderDetaillist(request):
    """
    List all, or create a new register
    """
    if request.method == 'GET':
            orderDet = orderDetail.objects.all()
            serializer = orderdetail_serializer(orderDet, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = orderdetail_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def orderDetaildetail(request, id):
    """
    Retrieve, update or delete a code orderDetail.
    """
    try:
        orderDet = orderDetail.objects.get(id=id)
    except orderDet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = orderdetail_serializer(orderDet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = orderdetail_serializer(orderDet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        orderDet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



