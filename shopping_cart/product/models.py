from django.db import models

# Create your models here.
class Product(models.Model):
    LIVE - 1
    DELETE - 0
    STATUS_CHOICES = (
        (LIVE, "Live"),
        (DELETE, "Delete"),
    )
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True,null=True)
    price = models.FloatField(default=0)
    img = models.ImageField(blank=True,null=True,upload_to='productpic/')
    priority = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
