from django.urls import path,include
from employee import views

# urlpatterns = [
# 	path('employee/',views.employee),
#       path('employee/<int:id>/', views.employee_details),
# ]

from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', views.EmployeeViewSet)
	
urlpatterns = [
	path('', include(router.urls)),
      # path('employee/',views.employee),
      # path('employee/<int:id>/', views.employee_details),
]