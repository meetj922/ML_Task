from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clients.views import ClientViewSet
from projects.views import ProjectViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]