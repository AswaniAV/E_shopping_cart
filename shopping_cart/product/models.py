from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(null=True,blank=True)
    desc = models.TextField(max_length=200)
    img = models.ImageField(upload_to='productpic')
    priority = models.IntegerField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
