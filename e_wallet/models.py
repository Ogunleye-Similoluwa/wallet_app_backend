from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True, max_length=11)


class Account(models.Model):
    bank_name = models.CharField(max_length=235)
    account_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=11, decimal_places=2)


class Card(models.Model):
    CARD_TYPE = [
        ('AMERICAN_EXPRESS', 'AMERICAN_EXPRESS'),
        ('VISA', 'VISA'),
        ('MASTERCARD', 'MASTERCARD'),
        ('VERVE', 'VERVE'),
    ]
    card_number = models.CharField(max_length=16)
    card_name = models.CharField(max_length=255)
    cvv = models.CharField(max_length=3)
    expiry_date = models.DateField(auto_created=True)
    card_type = models.CharField(max_length=20, choices=CARD_TYPE)


class Beneficiary(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('AIRTIME', 'AIRTIME'),
        ('TV', 'TV'),
        ('DATA', 'DATA'),
        ('ELECTRICITY', 'ELECTRICITY'),
        ('WATER', 'WATER'),
        ('EDUCATION', 'EDUCATION')
    ]
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now=True)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE)


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    card = models.OneToOneField(Card, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"{}"