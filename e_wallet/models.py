from django.db import models


class User(models.Model):
    user_id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=40, default="Full Name", null=False, blank=False)
    username = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    password = models.CharField(max_length=20, default="")
    phone_number = models.CharField(max_length=12, null=False, blank=False)
    date = models.DateTimeField(auto_now=True, null=False, blank=False)
    wallet = models.ForeignKey("Wallet", on_delete=models.CASCADE)
    notification = models.OneToOneField("Notification", on_delete=models.CASCADE)


class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('SEND MONEY', 'WITHDRAW', 'BUY AIRTIME', 'BUY DATA', 'PAY BILL')
    ]
    TRANSACTION_STATUS = [
        ('PENDING', 'SENT', 'FAILED')
    ]
    transaction_id = models.IntegerField(primary_key=True)
    transaction_type = models.CharField(blank=False, null=False, choices=TRANSACTION_TYPE)
    transaction_status = models.CharField(blank=False, null=False, choices=TRANSACTION_STATUS)
    amount = models.DecimalField(blank=False, null=False)
    date = models.DateTimeField(auto_now=True, null=False, blank=False)
    wallet = models.ManyToOneRel("Wallet", on_delete=models.CASCADE, related_name="wallet")
    notification = models.OneToOneField("Notification", on_delete=models.CASCADE)


class CreditCard(models.Model):
    card_id = models.IntegerField(primary_key=True)
    credit_card_number = models.IntegerField(null=False, blank=False, max_length=20)
    ccv = models.IntegerField(null=False, blank=False)
    expiry_date = models.DateTimeField(null=False, blank=False)


class Account(models.Model):
    account_id = models.IntegerField(primary_key=True)
    bank_name = models.CharField(max_length=20, null=False, blank=False)
    account_name = models.CharField(User.name)
    bank_number = models.CharField()


class Wallet(models.Model):
    wallet_id = models.IntegerField(primary_key=True, auto_created=True)
    balance = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


class Notification(models.Model):
    notification_id = models.IntegerField(primary_key=True, auto_created=True)
    message = models.CharField(max_length=200, null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now=True)


class Admin(models.Model):
    admin_id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(null=False, blank=False, max_length=200)
    username = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    password = models.CharField(max_length=20, default="")
