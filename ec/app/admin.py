from django.contrib import admin
from .models import Product, Customer, Cart, Payment, OrderPlaced, Wishlist
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.auth.models import Group

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    """klasė, kuri yra registruojama su "admin" moduliu. Ji turi "list_display" savybę, kuri nurodo, kokius laukus
     rodyti produkto sąraše administravimo panelėje. Laukai yra "id", "title", "discounted_price", "category" ir
     "product_image"."""
    list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    """administravimo srities klasė, kurioje nustatomas, kokie laukai bus rodomi "Customer" modelio sąraše. Tai
    reiškia, kad administravimo srityje vartotojai matys tik "id", "user", "locality", "zipcode" ir "city" laukus.
     Tai leidžia administravimo srities vartotojams greitai ir lengvai peržiūrėti ir valdyti vartotojų informaciją."""
    list_display = ['id', 'user', 'locality', 'zipcode', 'city']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    """ši klasė yra "CartModelAdmin" admin registratorius, kuris nustato, kaip "Cart" modelis bus rodomas
    administravimo srityje. "list_display" nustato, kokie laukai bus rodomi sąrašo puslapyje. "products" funkcija
    nurodo, kad "products" laukas bus rodomas kaip nuoroda į produkto redagavimo puslapį administravimo srityje.
    Format_html funkcija naudojama, kad suformuotų nuorodą su HTML formatu."""
    list_display = ['id', 'user', 'products', 'quantity']
    def products(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)


@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    """Klasė "PaymentModelAdmin" yra administratoriaus sąsaja, kurioje rodomi mokėjimo duomenys. Pateikiamos
    informacijos stulpeliai yra "id", "user" (vartotojas), "amount" (sumokėta suma), "pay_order_id" (užsakymo ID),
     "pay_payment_status" (mokėjimo būsena), "pay_payment_id" (mokėjimo ID) ir "paid" (ar sumokėta)."""
    list_display = ['id', 'user', 'amount', 'pay_order_id', 'pay_payment_status', 'pay_payment_id', 'paid']


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    """administratoriaus registracijos klasė užsakymų sąrašo modeliui. Tai rodo administratoriaus sąsajoje, kokie
    laukai bus rodomi užsakymo sąraše (id, vartotojas, klientas, produktai, kiekis, užsakymo data, būsena, mokėjimai).
     Be to, tai taip pat nurodo, kaip bus rodomas kiekvieno produkto ir mokėjimo pavadinimas administratoriaus sąsajoje
      (kaip nuoroda į produkto ar mokėjimo redagavimo puslapį)."""
    list_display = ['id', 'user', 'customers', 'products', 'quantity', 'ordered_date', 'status', 'payments']
    def customers(self, obj):
        link = reverse("admin:app_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)
    def products(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)
    def payments(self, obj):
        link = reverse("admin:app_payment_change", args=[obj.payment.pk])
        return format_html('<a href="{}">{}</a>', link, obj.payment.pay_payment_id)


@admin.register(Wishlist)
class WishlistdModelAdmin(admin.ModelAdmin):
    """administravimo srities klasė, kurioje registruojamas "Wishlist" modelis. "list_display" atributas nurodo,
    kokie laukai turėtų būti rodomi administraciniame puslapyje, kai yra rodomi "Wishlist" įrašai. Taip pat yra
    metodas "products", kuris susieja "Wishlist" įrašo produktą su administravimo srities produktų puslapiu. Taigi,
     kai administratorius paspaudžia produkto pavadinimą, jis nukreipiamas į produkto redagavimo puslapį
     administravimo srityje."""
    list_display = ['id', 'user', 'products']
    def products(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)


admin.site.unregister(Group)


