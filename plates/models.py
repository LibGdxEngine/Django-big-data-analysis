from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Plate(models.Model):
    image_path = models.CharField(max_length=220)
    image_time = models.CharField(max_length=8)
    predicted_code = models.CharField(max_length=4)
    predicted_number = models.CharField(max_length=10)
    predicted_emirate = models.CharField(max_length=10)
    predicted_color = models.CharField(max_length=10)
    gt_code = models.CharField(max_length=4)
    gt_number = models.CharField(max_length=10)
    gt_emirate = models.CharField(max_length=10)
    gt_color = models.CharField(max_length=10)
    csv_file = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    status = models.PositiveIntegerField()

    def __str__(self):
        return self.image_path
