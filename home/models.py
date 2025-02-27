from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='phone_images/')

    def __str__(self):
        return f"{self.name}, {self.price}"

    class Meta:
        ordering = ['-created_at']

class Laptop(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='laptop_images/')

    def __str__(self):
        return f"{self.name}, {self.price}"

    class Meta:
        ordering = ['-created_at']

class Watch(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='watch_images/')

    def __str__(self):
        return f"{self.name}, {self.price}"

    class Meta:
        ordering = ['-created_at']

