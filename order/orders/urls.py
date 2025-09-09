from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, index
from . import views

router = DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', index, name='index.html'),
    path('admin45/', views.admin , name='admin.html'),  # HTML page
]

urlpatterns += router.urls