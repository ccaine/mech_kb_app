from django.db import models


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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    gb_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    gb_type = models.CharField(max_length=20, choices=TYPE_CHOICES)


