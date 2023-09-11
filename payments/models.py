from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    reference = models.CharField(max_length=200, unique=True)  # Unique reference provided by Paystack for each transaction
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount to be paid in the smallest unit of your currency. E.g., cents for USD
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('success', 'Success'), ('failed', 'Failed')])
    email = models.EmailField()  # The email of the user making the payment
    metadata = models.JSONField(null=True, blank=True)  # Any additional data you might want to store, like items purchased, etc.
    payment_date = models.DateTimeField(auto_now_add=True)  # Date the payment was initiated

    class Meta:
        ordering = ['-payment_date']

    def __str__(self):
        return f"{self.user} - {self.amount} - {self.status}"

class TransactionVerification(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, related_name='verification')
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('success', 'Success'), ('failed', 'Failed')])
    message = models.TextField(null=True, blank=True)  # Any message or description from Paystack after verification
    verified_at = models.DateTimeField(null=True, blank=True)  # Date the transaction was verified

    def __str__(self):
        return f"{self.payment.reference} - {self.status}"
