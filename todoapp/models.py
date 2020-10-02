from django.db import models
from django.utils import timezone
# Create your models here.

class ToDoItem(models.Model):
    text = models.TextField()
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)

    def complete(self):
        self.completed = True
        self.save()

    def __str__(self):
        return self.text