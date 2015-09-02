from django.db import models

# Create your models here.
from django.db import models

# Create your Django models here, if you need them.
class Mileage(models.Model):
    start_mileage = models.PositiveIntegerField(null=False, default=0)
    start_time = models.DateTimeField(null=True)
    stop_mileage = models.PositiveIntegerField(null=False, default=0)
    stop_time = models.DateTimeField(null=True)
    reporter = models.CharField(null=False, max_length=20)
    completed = models.BooleanField(default=False)