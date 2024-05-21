from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirmpassword = models.CharField(max_length=100)


class Customer(models.Model):
    LIVE = 1
    DELETE = 0
    STATUS_CHOICES = (
        (LIVE,"Live"),
        (DELETE, "Delete"), 
    )
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    user = models.OneToOneField(User, related_name="customer", on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    img = models.ImageField(blank=True, null= True, upload_to='customers/')
    email = models.EmailField(default="example@example.com")
    priority = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE)
    created_at = models.DateField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True, editable=False)

    def __str__(self):
        return self.user.username
    

