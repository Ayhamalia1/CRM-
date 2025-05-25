from django.db import models 
from django.contrib.auth.models import AbstractUser


class Service(models.Model):
   name=models.CharField(max_length=20)
   description=models.TextField(max_length=100)
   price=models.DecimalField(max_digits=5 ,decimal_places=2)
   is_active=models.BooleanField(default=True)
   
   def __str__(self):
      return self.name
   #Customer model
class Customer(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    address=models.CharField(max_length=50,default="")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    services = models.ManyToManyField(
        Service,
        through='CustomerService',
        through_fields=('customer', 'service'),
        related_name='customers'
    )   
    def __str__(self):
     return self.name
# intermidate model

class CustomerService(models.Model):
   customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
   service = models.ForeignKey(Service, on_delete=models.CASCADE)
   start_date = models.DateField(auto_now_add=True)
   end_date = models.DateField(null=True,blank=True)

   def __str__(self):
      return f"{self.customer.name} - {self.service.name}"
   
CHOICES = [
    ('IT', 'IT'),
    ('Support', 'Support'),
    ('Sales', 'Sales'),  
]
class User(AbstractUser):
  department=models.CharField(max_length=20,choices=CHOICES)
def __str__(self):  
     return self.username
