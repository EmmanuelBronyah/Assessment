from django.db import models


class User(models.Model):

    class Role(models.TextChoices):
        ADMIN = "admin"
        VENDOR = "vendor"
        CUSTOMER = "customer"

    name = models.CharField(max_length=125)
    role = models.CharField(max_length=10, choices=Role)

    def __str__(self):
        return f"Name: {self.name} Role: {self.role}"
