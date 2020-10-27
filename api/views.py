from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BrandSerializer, ParentSerializer
from nestle.models import Brand, Parent
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('BRAND_NAME')
    serializer_class = BrandSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['BRAND_NAME', 'PARENT_BRAND__PARENT_BRAND']
    #NOTE TO SELF: CANNOT ACCESS FOREIGNKEY FIELD.
    #MUST POINT DJANGO TO THE FIELD OF THE FOREIGNKEY FIELD
    #THAT YOU WANT TO ACCESS


class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
