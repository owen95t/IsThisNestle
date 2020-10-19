from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BrandSerializer, ParentSerializer
from nestle.models import Brand, Parent

# Create your views here.
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('BRAND_NAME')
    serializer_class = BrandSerializer

class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer