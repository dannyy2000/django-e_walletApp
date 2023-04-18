from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

from wallet.models import Wallet


# class WalletSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Wallet
#         fields = ('id', 'balance')


class DashboardSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    balance = serializers.FloatField(source='Wallet.balance', read_only=True)

    class Meta:
        model = Wallet
        fields = ('username', 'balance')


class UserCreate(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'phone_number', 'first_name', 'last_name']
