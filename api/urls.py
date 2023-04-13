from django.urls import path, include
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register('Wallet_View', WalletView)

urlpatterns = [
    path('', include(router.urls)),

]