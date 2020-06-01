from django.db import models

# pizza menu model to include regular and sicilian
class Pizza(models.Model):
      typ = models.CharField(max_length=10)
      category = models.CharField(max_length=10)
      size = models.CharField(max_length=5)
      price = models.DecimalField(max_digits=4, decimal_places=2)

      def __str__(self):
          return f"{self.typ} {self.category} {self.size} -- ${self.price}"


# pizza toppings model
class Toppings(models.Model):
      name = models.CharField(max_length=64)

      def __str__(self):
          return f"{self.name}"


# pizza orders
class PizItem(models.Model):
      typ = models.CharField(max_length=10)
      category = models.CharField(max_length=10)
      size = models.CharField(max_length=5)
      price = models.DecimalField(max_digits=4, decimal_places=2)
      top1 = models.ForeignKey(Toppings, null=True, on_delete=models.SET_NULL, related_name="topping1")
      top2 = models.ForeignKey(Toppings, null=True, on_delete=models.SET_NULL, related_name="topping2")
      top3 = models.ForeignKey(Toppings, null=True, on_delete=models.SET_NULL, related_name="topping3")

      def __str__(self):
          return f"{self.typ} {self.category} {self.size} + {self.top1} + {self.top2} + {self.top3} -- ${self.price}"