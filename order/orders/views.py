from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def admin(request):
    return render(request, 'admin.html')

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-time')
    serializer_class = OrderSerializer

    @action(detail=True, methods=['post'], url_path='complete')
    def complete(self, request, pk=None):
        order = self.get_object()
        if order.status != 'completed':
            order.status = 'completed'
            order.save()
            return Response({'status': 'Order marked as completed'})
        return Response({'status': 'Order was already completed'})
