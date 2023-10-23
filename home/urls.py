from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path(''       , views.index,  name='index'),
  path('tables/', views.tables, name='tables'),
  path('calendar/', views.sample_page, name='sample_page'),
  path('tab/', views.tab_page, name='tab'),
]