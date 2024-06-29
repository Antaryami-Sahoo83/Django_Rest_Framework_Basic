from django.urls import path, include
from rest_framework import routers

from user import views

router = routers.DefaultRouter()
router.register('user', views.UserViewSet, basename='employee')
	
urlpatterns = [
	path('user/', include(router.urls))	
]