from django.urls import path
from rest_framework import routers
from .views import ProjecViewSet

router = routers.DefaultRouter()
router.register('api/projects', ProjecViewSet, 'projects')

urlpatterns = router.urls