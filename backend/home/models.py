from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Review(models.Model):
    "Generated Model"
    description = models.CharField(max_length=256,)
    email = models.EmailField(max_length=254,)
    phone = models.CharField(max_length=256,)
    reviewer = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="review_reviewer",
    )
