from django.db import models

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
class Orderitems(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return f"{self.food.name} - {self.quantity}"
    # def total_price(self):
    #     return self.food.price * self.quantity   

class Order(models.Model):
    
    order_items = models.ForeignKey(Orderitems, on_delete=models.CASCADE)
    total_price = models.IntegerField()   
    status = models.BooleanField(default=False)
    payment_status = models.BooleanField(default=False)
    def __str__(self):
        return f"Order {self.order_items} - Total: {self.total_price}"

    

