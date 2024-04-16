from django.db import models
from users.models import Profile
import uuid

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='tasks')
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    