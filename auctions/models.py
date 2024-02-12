from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name=models.CharField(max_length=20,default=1)
    def __str__(self):
        return self.name

# This is my listing model
class Listing(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=500,null=True,blank=True)
    starting_bid=models.ForeignKey('Bid',on_delete=models.CASCADE)
    comments=models.CharField(max_length=500)
    active=models.BooleanField()
    image=models.CharField(max_length=2000)
    wachlist=models.ManyToManyField(User,related_name='wachlists',blank=True,null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return f"Title is {self.title} and price is {self.starting_bid}"
    


class Bid(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    bid_amount=models.DecimalField(decimal_places=2,max_digits=10)
    bid_time=models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)  
    def __str__(self):
        return f"{self.bid_amount}"
    