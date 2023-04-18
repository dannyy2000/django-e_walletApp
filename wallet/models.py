from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class WalletUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, blank=False, null=False, unique=True)
    upload_image = models.ImageField(upload_to='user_photos/', default=None)
    cloudinary_public_id = models.CharField(max_length=100, blank=True)


class Account(models.Model):
    bank_name = models.CharField(max_length=30, blank=False, null=False)
    account_number = models.CharField(max_length=11, blank=False, null=False)

    def __str__(self):
        return self.bank_name


class Card(models.Model):
    card_number = models.CharField(max_length=16)
    card_name = models.CharField(max_length=30)
    expiry_date = models.DateField()
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return self.card_name


class Beneficiary(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('DEPOSIT', 'DEP'),
        ('WITHDRAWAL', 'WIT'),
        ('AIRTIME', 'AIR'),
        ('BILL', 'BIL'),
        ('DATA', 'DAT')
    ]

    account = models.ForeignKey(Account, on_delete=models.PROTECT, default=None)
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)


class Wallet(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='account')
    wallet_user = models.OneToOneField(WalletUser, on_delete=models.CASCADE)
    card = models.OneToOneField(Card, on_delete=models.CASCADE, default=None)
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE, default=None)
    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT, default=None)


class Notification(models.Model):
    message = models.CharField(max_length=50, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE, related_name='transaction')
    wallet_user = models.OneToOneField(WalletUser, on_delete=models.CASCADE)
