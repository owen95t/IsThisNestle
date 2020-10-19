from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:parent_id>/', views.detail),
    path('<int:brand_id>/results', views.results),
    path('allbrands/', views.allbrands),
    path('allparents/', views.parent, name='parent'),
    path('search/', views.search, name='search')

]