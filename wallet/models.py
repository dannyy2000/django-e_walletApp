from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class WalletUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Account(models.Model):
    bank_name = models.CharField(max_length=30, blank=False, null=False)
    account_name = models.CharField(max_length=20, blank=False, null=False)
    account_number = models.CharField(max_length=11, blank=False, null=False)


class CreditCard(models.Model):
    card_number = models.IntegerField()
    expiry_date = models.DateTimeField(auto_now_add=True)
    cvv = models.IntegerField()


class Wallet(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='account')
    wallet_user = models.ForeignKey(WalletUser, on_delete=models.CASCADE)
    credit_card = models.OneToOneField(CreditCard, on_delete=models.CASCADE)


class Beneficiary(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,default=1)


class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('DEPOSIT', 'DEP'),
        ('WITHDRAWAL', 'WIT'),
        ('AIRTIME', 'AIR'),
        ('BILL', 'BIL'),
        ('DATA', 'DAT')
    ]

    TRANSACTION_STATUS = [
        ('SUCCESSFUL', 'SUC'),
        ('PENDING', 'PEN'),
        ('FAILED', 'FAI')
    ]

    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPE)
    transaction_status = models.CharField(max_length=15, choices=TRANSACTION_STATUS)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='wallet')
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE, related_name='beneficiary')


class Notification(models.Model):
    message = models.CharField(max_length=50, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE, related_name='transaction')
    wallet_user = models.OneToOneField(WalletUser, on_delete=models.CASCADE)
