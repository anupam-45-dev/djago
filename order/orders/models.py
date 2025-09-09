

from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('completed', 'Completed'),
    ]
    name = models.CharField(max_length=100)
    table = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    items = models.JSONField()
    sub_total = models.FloatField()
    gst_total = models.FloatField()
    total = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.name}"
