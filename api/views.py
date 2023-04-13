from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from e_wallet.models import *
from api.serializers import *


# Create your views here.

class WalletView(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
