from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class ToDoItem(models.Model):
    text = models.TextField()
    completed = models.BooleanField(default=False)
    urgent = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)

    def complete(self):
        self.completed = True
        self.save()

    def published_recently(self):
        result = self.date_created >= timezone.now() - datetime.timedelta(days=1)
        return result

    def __str__(self):
        return self.text