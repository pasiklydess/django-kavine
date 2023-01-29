from django.db import models
from django.contrib.auth.models import User

# Create your models here.


CATEGORY_CHOICES = (
    ('PZ', 'Pizza'),
    ('DR', 'Drinks'),
    ('BR', 'Burgers'),
    ('PS', 'Pasta'),
)


class Product(models.Model):
    """ tai modelis, kuris aprašo produktus, kuriuos siūlo mūsų restoranas. Jame yra laukai: pavadinimas,
    pardavimo kaina, nuolaidos kaina (jei yra), aprašymas, sudėtis, kategorija ir produkto paveikslėlis."""
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField(null=True)
    description = models.TextField()
    composition = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title


class Customer(models.Model):
    """ tai modelis, kuris aprašo mūsų restorano klientus. Jame yra laukai: vartotojas, vardas,
     mobilusis telefonas, vietovė, pašto kodas ir miestas."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mobile = models.IntegerField(default=+3706)
    locality = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Cart(models.Model):
    """ tai modelis, kuris aprašo produktus, kuriuos vartotojas pasirinko pirkti. Jame yra laukai: vartotojas,
     produktas, kiekis ir bendra suma."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
    ('Pending', 'Pending'),
)


class Payment(models.Model):
    """tai modelis, kuris aprašo mokėjimus, kuriuos vartotojas atliko. Jame yra laukai: vartotojas, suma,
     užsakymo ID, mokėjimo būsena, mokėjimo ID ir ar mokėjimas buvo atliktas."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    pay_order_id = models.CharField(max_length=100, blank=True, null=True)
    pay_payment_status = models.CharField(max_length=100, blank=True, null=True)
    pay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)


class OrderPlaced(models.Model):
    """ tai modelis, kuris aprašo užsakymus, kuriuos vartotojas padarė. Jame yra laukai: vartotojas,
    klientas, produktas, kiekis, užsakymo data, būsena ir mokėjimas."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="")

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price



class Wishlist(models.Model):
    """tai modelis, kuris aprašo produktus, kuriuos vartotojas nori pirkti ateityje.
    Jame yra laukai: vartotojas ir produktas."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
