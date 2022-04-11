from rest_framework.routers import DefaultRouter
from .views import JobViewSet

User_router = DefaultRouter()
User_router.register('parttwo', JobViewSet)
