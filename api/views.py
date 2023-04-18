from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsAdminOrReadOnly
from api.serializers import DashboardSerializer
from wallet.models import Wallet


# Create your views here.

class DashBoardView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Wallet.objects.all()
    serializer_class = DashboardSerializer

