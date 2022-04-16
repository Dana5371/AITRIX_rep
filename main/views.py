from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubcategoryListView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class =SubcategorySerializer


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
