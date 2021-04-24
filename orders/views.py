from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .serializers import OrderSerializer
from .models import Order

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]
    lookup_field = 'order_number'
        
