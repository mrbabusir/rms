from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)    
    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
class Table(models.Model):    
    table_number = models.IntegerField()
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} - Capacity: {self.capacity} - Available: {self.is_available}"

class Order(models.Model):
    PENDING = 'P'
    COMPLETED = 'C'
    DELIVERED = 'D'
    STATUS_CHOICE = {
        PENDING : 'Pending',
        COMPLETED : 'Completed',
        DELIVERED : 'Delivered',
    }

    PAID = 'P'
    UNPAID = 'U'
    PAYMENT_STATUS_CHOICE = {
        PAID : 'Paid',
        UNPAID : 'Unpaid',
        }    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField()   
    food_status = models.CharField(max_length=1, choices = STATUS_CHOICE, default=PENDING)
    payment_status = models.CharField(max_length=1, choices= PAYMENT_STATUS_CHOICE, default=UNPAID)
    
    def __str__(self):
        return f"Order by {self.user} - Total: {self.total_price} - Food Status: {self.food_status} - Payment Status: {self.payment_status}"

    

class Orderitems(models.Model):
    food = models.ForeignKey(Food, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)    
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"Foods {self.food} - {self.quantity} - {self.order}"