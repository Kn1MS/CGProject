from django.db import models
from datetime import datetime

# Create your models here.

class NumberGenerateTask(models.Model):
	time = models.DateTimeField(default = datetime.now)
	status = models.CharField(max_length = 30, default = "Pending")
	result = models.IntegerField(default = 0)