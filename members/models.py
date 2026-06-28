from django.db import models
# from django.utils.text import slugify
from autoslug import AutoSlugField

from uuid import uuid4
# Create your models here.

class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    # slug = models.SlugField(default="", null=False, )
    
    def get_full_name(self):
        return f"{self.first_name}-{self.last_name}"

    slug = AutoSlugField(
        populate_from="get_full_name",
        unique=True,
        always_update=False,
    )
    
    # def save(self, *args, **kwargs):

    #     if not self.slug:
    #         self.slug = slugify(f"{self.first_name}-{self.last_name}")

    #     super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.first_name} - {self.last_name}"