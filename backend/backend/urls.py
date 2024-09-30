from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from votes.views import PersonViewSet, BillViewSet

router = DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'bills', BillViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
