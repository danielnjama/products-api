# views.py
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import userinfo, productCategory, products
from .serializers import UserInfoSerializer, ProductCategorySerializer, productsSerializer,UserSerializer

from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token


class CustomRegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token, _ = Token.objects.get_or_create(user=user)  # Use Token model here
                return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)




class UserInfoListCreate(generics.ListCreateAPIView):
    queryset = userinfo.objects.all()
    serializer_class = UserInfoSerializer
    #authentication_classes = [BasicAuthentication]
#    permission_classes = [IsAuthenticated]

class UserInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = userinfo.objects.all()
    serializer_class = UserInfoSerializer
    #authentication_classes = [BasicAuthentication]
#    permission_classes = [IsAuthenticated]

class ProductCategoryListCreate(generics.ListCreateAPIView):
    queryset = productCategory.objects.all()
    serializer_class = ProductCategorySerializer
    #authentication_classes = [BasicAuthentication]
#    permission_classes = [IsAuthenticated]

class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = productCategory.objects.all()
    serializer_class = ProductCategorySerializer
    #authentication_classes = [BasicAuthentication]
#    permission_classes = [IsAuthenticated]

class ProductListCreate(generics.ListCreateAPIView):
    queryset = products.objects.all()
    serializer_class = productsSerializer
    #authentication_classes = [BasicAuthentication]
#    permission_classes = [IsAuthenticated]

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = products.objects.all()
    serializer_class = productsSerializer
    #authentication_classes = [BasicAuthentication]
#    permission_classes = [IsAuthenticated]






























# from django.shortcuts import render
# from rest_framework import generics
# from .models import userinfo, productCategory, products
# from .serializers import UserInfoSerializer, ProductCategorySerializer, productsSerializer
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

# class UserInfoList(generics.ListCreateAPIView):
#     queryset = userinfo.objects.all()
#     serializer_class = UserInfoSerializer
#     # authentication_classes = [BasicAuthentication]
#     # permission_classes = [IsAuthenticated]

# class ProductCategoryList(generics.ListCreateAPIView):
#     queryset = productCategory.objects.all()
#     serializer_class = ProductCategorySerializer
#     # authentication_classes = [BasicAuthentication]
#     # permission_classes = [IsAuthenticated]

# class ProductList(generics.ListCreateAPIView):
#     queryset = products.objects.all()
#     serializer_class = productsSerializer
#     # authentication_classes = [BasicAuthentication]
#     # permission_classes = [IsAuthenticated]

