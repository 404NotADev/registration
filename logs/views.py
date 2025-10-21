from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import LoginLog
from .serializers import LoginLogSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
import django_filters

class LoginLogFilter(django_filters.FilterSet):
    start_date = django_filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_date = django_filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')
    user_id = django_filters.NumberFilter(field_name="user__id")

    class Meta:
        model = LoginLog
        fields = ['user_id', 'start_date', 'end_date']

class LoginLogListView(generics.ListAPIView):
    queryset = LoginLog.objects.all().order_by('-timestamp')
    serializer_class = LoginLogSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = LoginLogFilter
    ordering_fields = ['timestamp']

