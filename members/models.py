from django.db import models
from uuid import uuid4
# Create your models here.

class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(default="", null=False)
    
    def __str__(self):
        return f"{self.first_name} - {self.last_name}"