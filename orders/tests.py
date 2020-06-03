from django.test import TestCase

from orders.models import Orders, Pizza, Toppings, Sub, Extras, Pasta, Salad, Platter

# Create your tests here.
# class ModelsTestCase(TestCase):

#     def setUp(self):

#         # Create pizzas
#         p1 = Pizza.objects.create(typ='Regular', category='Cheese', size='small', price='12.70')
#         p2 = Pizza.objects.create(typ='Regular', category='2 topping', size='small', price='15.20')
#         p3 = Pizza.objects.create(typ='Regular', category='2 topping', size='large', price='21.95')
#         p4 = Pizza.objects.create(typ='Sicilian', category='3 item', size='large', price='44.70')

#         # Create toppings
#         Pepperoni = Toppings.objects.create(typ='Pepperoni')
#         Sausage = Toppings.objects.create(typ='Sausage')
#         Mushrooms = Toppings.objects.create(typ='Mushrooms')
#         Onions = Toppings.objects.create(typ='Onions')
#         Ham = Toppings.objects.create(typ='Ham')
#         CanadianBacon = Toppings.objects.create(typ='Canadian Bacon')
#         Pineapple = Toppings.objects.create(typ='Pineapple')
    
    
#     def loaded(self):
#         t = Toppings.objects.all()
#         p = Pizza.objects.all()
#         self.assertEqual(t.count(), 7)
#         self.assertEqual(p.count(), 4)

    # # test adding 2 topping to a pizza
    # def test_toppings_add1(self):
    #     p = Pizza.objects.get(typ='Regular', category='2 topping', size='small', price='15.20')
    #     pepperoni = Toppings.objects.get(typ='Pepperoni')
    #     sausage = Toppings.objects.get(typ='Sausage')
    #     p.toppings.add(pepperoni)
    #     p.toppings.add(sausage)
    #     self.assertEqual(p.toppings.count(), 2)
    
    # # check that original with no toppings still exists
    # def test_toppings_add2(self):
    #     self.assertEqual(p2.toppings.count(), 0)
