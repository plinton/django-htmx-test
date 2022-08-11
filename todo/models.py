from django.db import models

# Create your models here.
class TodoItem(models.Model):
    description = models.CharField(max_length=250)
    done_at = models.DateTimeField(null=True)
