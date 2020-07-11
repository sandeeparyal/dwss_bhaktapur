from django.urls import path
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [ 
        path('', views.index, name='index'),
#        path('employee_add/', views.employee_add, name='employee_add'),
        path('employee_list/', views.employee_list, name='employee_list'),
#        path('<employee_id>/employee_edit/', views.employee_edit, name='employee_edit'),
#        path('<employee_id>/employee_delete/', views.employee_delete, name='employee_delete'),
#        path('senior_employee/', views.senior_employee, name='senior_employee'),
#        path('fibonacci_gen/', views.fibonacci_gen, name='fibonacci_gen'),
] 
