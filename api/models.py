from django.db import models


class User(models.Model):

    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        VENDOR = "vendor", "Vendor"
        CUSTOMER = "customer", "Customer"

    name = models.CharField(max_length=125)
    role = models.CharField(max_length=10, choices=Role.choices)

    def __str__(self):
        return f"Name: {self.name} Role: {self.role}"
