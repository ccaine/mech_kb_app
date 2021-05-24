from django.db import models

from django.utils import timezone
from datetime import datetime

class GroupBuy(models.Model):

    STATUS_CHOICES = [
        ('UP', 'Upcoming'),
        ('SKIP', 'Skipped'),
        ('WAIT', 'Waiting'),
        ('REC', 'Received'),
        ('CANCEL', 'Canceled')
    ]

    TYPE_CHOICES = [
        ('KB', 'Keyboard'),
        ('KC', 'Keycaps'),
        ('ART', 'Artisan'),
        ('CB', 'Cables'),
    ]

    gb_name = models.CharField(max_length=200)
    gb_start = models.DateField(default=timezone.now)
    gb_end = models.DateField(default=timezone.now)

    gb_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    gb_type = models.CharField(max_length=20, choices=TYPE_CHOICES)


