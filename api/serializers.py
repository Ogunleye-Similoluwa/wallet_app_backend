from rest_framework import serializers
from e_wallet.models import *
from djoser.serializers import UserCreateSerializer as CreateSerializer


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['user', 'balance', 'account', 'card']


class UserCreateSerializer(CreateSerializer):
    class Meta(CreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']
