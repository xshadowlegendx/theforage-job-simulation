
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    address = models.TextField(null=True)
    membership = models.CharField(max_length=32, null=True)
    date_joined = models.DateTimeField(null=True)

    class Meta:
        db_table = 'user'

class AppUsage(models.Model):
    user = models.ForeignKey(
        User,
        blank=False,
        on_delete=models.PROTECT)

    clicks = models.IntegerField()
    timestamp = models.DateTimeField()
    session_end = models.DateTimeField()
    session_start = models.DateTimeField()
    pages_visited = models.TextField()
    device = models.CharField(max_length=64)
    usage_type = models.CharField(max_length=32)

    class Meta:
        db_table = 'app_usage'

class Transaction(models.Model):
    sender = models.ForeignKey(
        User,
        blank=False,
        related_name='sender_id',
        on_delete=models.PROTECT)

    recipient = models.ForeignKey(
        User,
        blank=False,
        related_name='recipient_id',
        on_delete=models.PROTECT)

    amount = models.DecimalField(decimal_places=16, max_digits=32)
    timestamp = models.DateTimeField()
    status = models.CharField(max_length=32)
    transaction_type = models.CharField(max_length=64)

    class Meta:
        db_table = 'transactions'
