from django.test import TestCase

from .models import Orders, Pizza, Toppings, Sub, Extras, Pasta, Salad, Platter

# Create your tests here.
class ModelsTestCase(TestCase):

    def setUp(self):

    # Create pizzas
    p1 = Pizza.objects.create(typ='Regular', category='Cheese', size='small', price='12.70')
    p2 = Pizza.objects.create(typ='Regular', category='2 topping', size='small', price='15.20')
    p3 = Pizza.objects.create(typ='Regular', category='2 topping', size='large', price='21.95')
    p4 = Pizza.objects.create(typ='Sicilian', category='3 item', size='large', price='44.70')

    # Create toppings
    Toppings.objects.create(typ='Pepperoni')
    Toppings.objects.create(typ='Sausage')
    Toppings.objects.create(typ='Mushrooms')
    Toppings.objects.create(typ='Onions')
    Toppings.objects.create(typ='Ham')
    Toppings.objects.create(typ='Canadian Bacon')
    Toppings.objects.create(typ='Pineapple')

    # test adding 2 topping to a pizza
    def test_toppings_add1(self):
        p = Pizza.objects.get(typ='Regular', category='2 topping', size='small')
        p = p.toppings.add()
        self.assertEqual(p.toppings.count(), 2)
    
    # check that original with no toppings still exists
    def test_toppings_add2(self):
        p = Pizza.objects.get(typ='Regular', category='2 topping', size='small')
        self.assertEqual(p.toppings.count(), 0)