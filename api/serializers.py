from rest_framework import serializers
from e_wallet.models import *
from djoser.serializers import UserCreateSerializer as CreateSerializer


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['bank_name', 'account_number', 'amount']
        bank_name = models.CharField(max_length=235)
        account_number = models.CharField(max_length=15)
        amount = models.DecimalField(max_digits=11, decimal_places=2)


class UserCreateSerializer(CreateSerializer):
    class Meta(CreateSerializer.Meta):
        fields = ['id', 'username', 'phone', 'email', 'password', 'first_name', 'last_name']


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = []


class WalletSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = Wallet
        fields = ['user', 'balance', 'account', 'card']
