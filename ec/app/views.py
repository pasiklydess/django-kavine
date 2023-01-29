# "from django.shortcuts" - ši biblioteka suteikia keletą paprastų funkcijų, kurios pagreitina ir
# supaprastina vartotojo sąsajos kūrimą.
# "render" - ši funkcija padeda atvaizduoti HTML failus.
# "redirect" - ši funkcija nukreipia vartotoją į kitą puslapį.
from django.shortcuts import render, redirect
# "View" - ši klasė yra bazinė klasė, kurios pagrindu kuriame savo views.
from django.views import View
# "models" - ši biblioteka leidžia susisiekti su duomenų baze ir valdyti jos informaciją.
# "Product, Customer, Cart, OrderPlaced, Payment, Wishlist" - tai yra modelių klasės, kurių pagrindu kuriame
# duomenų bazės lenteles.
from .models import Product, Customer, Cart, OrderPlaced, Payment, Wishlist
# "forms" - ši biblioteka leidžia sukurti formas vartotojui, kurie leidžia vartotojui pateikti informaciją.
# "CustomerRegistrationForm, CustomerProfileForm" - tai yra formų klasės, kurias naudojame vartotojų registracijai
# ir profilio atnaujinimui.
from .forms import CustomerRegistrationForm, CustomerProfileForm
# "messages" - ši biblioteka leidžia rodyti pranešimus vartotojui, pavyzdžiui, kai jis sėkmingai užsiregistravo.
from django.contrib import messages
# "JsonResponse" - ši klasė leidžia atvaizduoti rezultatus kaip JSON formate.
from django.http import JsonResponse
# "Q" - ši klasė leidžia atlikti sudėtingesnius paieškos užklausas.
from django.db.models import Q
# "login_required" - ši dekoratoriaus funkcija reikalauja, kad vartotojas būtų prisijungęs, kad
# galėtų pasiekti tam tikrus puslapius.
from django.contrib.auth.decorators import login_required
# "method_decorator" - ši funkcija leidžia naudoti dekoratorius su klasėmis (pvz., views).
from django.utils.decorators import method_decorator



# Create your views here.
@login_required
def home(request):
    """Ši funkcija yra skirta pagrindinio puslapio (home) atvaizdavimui. Pirma, funkcija patikrina ar vartotojas
    yra prisijungęs. Jei taip, tai funkcija suskaičiuoja kiek produktų yra vartotojo krepšelyje ir kiek produktų
    yra vartotojo pageidavimų sąraše. Po to funkcija naudoja "render" funkciją kad atvaizduotų pagrindinio puslapio
    template'ą (app/home.html) ir perduoda kintamuosius "totalitem" ir "wishitem" kaip locals() funkcijos parametrus."""
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "app/home.html", locals())


@login_required
def about(request):
    """"Šis kodas yra funkcija "about", kuri yra susijusi su naudotojo prisijungimo reikalavimu. Jei naudotojas
    yra prisijungęs, funkcija suskaičiuoja visus produktus, esančius naudotojo krepšelyje ir produktus, kuriuos
    naudotojas yra įtraukęs į pageidavimų sąrašą. Tada funkcija naudoja "render" funkciją, kad parodytų
    "app/about.html" puslapį su "totalitem" ir "wishitem" kintamųjais, kurie yra susiję su krepšelio ir
    pageidavimų sąrašo produktų skaičiumi. Taip pat funkcija "about" parodo apie puslapį."""
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "app/about.html", locals())


@login_required
def contact(request):
    """Šie trys kodų fragmentai yra "view" funkcijos, kurios yra atsakingos už kiekvieno puslapio
    (home, about, contact) atvaizdavimą. Funkcijos pradeda su @login_required, kas reiškia, kad vartotojas turi
     būti prisijungęs, kad galėtų matyti šiuos puslapius. Tada funkcijos nustato du kintamuosius - totalitem ir
     wishitem. Jei vartotojas yra prisijungęs, šie kintamieji bus nustatyti kaip "Cart" ir "Wishlist" objektų,
     esančių vartotojo, kiekis. Galiausiai funkcijos sukuria "render" funkciją, kuri atvaizduoja reikiamą HTML
      puslapį ir perduoda "locals()" kintamuosius, kad jie būtų naudojami puslapyje."""
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "app/contact.html", locals())


@method_decorator(login_required, name='dispatch')
class CategoryView(View):
    """Klasė "CategoryView" yra "View" klasės subklasė, kuri reikalauja prisijungimo
    (naudojant "login_required" dekoratorių), kad būtų galima pasiekti jos metodus. Metode "get" yra nustatomas
    produktų skaičius krepšelyje ir pageidavimų sąraše, jei vartotojas yra prisijungęs. Taip pat yra gaunami
    produktai ir jų pavadinimai, kurių kategorija yra nurodyta "val" kintamajame, ir jie yra atvaizduojami
    "category.html" šablone."""

    def get(self, request, val):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html", locals())


@method_decorator(login_required, name='dispatch')
class CategoryTitle(View):
    """Ši klasė yra skirta produktų kategorijų puslapių atvaizdavimui. Jai taikomas "login_required" dekoratorius,
     kuris reikalauja, kad vartotojas būtų prisijungęs, kad galėtų matyti kategorijų puslapius. Metodas "get"
     išfiltruoja produktus pagal jų kategorijos pavadinimą ir atvaizduoja juos "app/category.html" šablono pagalba.
      Taip pat skaičiuoja ir atvaizduoja prisijungusio vartotojo "Cart" ir "Wishlist" prekių skaičių."""

    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, "app/category.html", locals())


@method_decorator(login_required, name='dispatch')
class ProductDetail(View):
    """@method_decorator reiškia, kad šiam klasės metodui yra pritaikytas papildomas "dekoratorius" login_required,
     kuris reikalauja, kad vartotojas būtų prisijungęs, kad galėtų matyti produkto detalų. Klasė ProductDetail yra
     paveldinti iš View klasės ir turi metodą get, kuris gauna produkto informaciją pagal nurodytą "pk" ir atvaizduoja
      ją vartotojui. Taip pat tikrinama, ar vartotojas yra prisijungęs ir jei taip, tikrinama, kiek produktų yra
      jo norų sąraše ir krepšelyje. Galiausiai, perduodami duomenys atvaizduojami "app/product_detail.html" šablone."""

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, "app/product_detail.html", locals())


class CustomerRegistrationView(View):
    """Klasė CustomerRegistrationView paveldi iš View klasės ir turi metodus get ir post. Metodas get yra atsakingas
     už formos atvaizdavimą vartotojui ir tikrina, ar vartotojas yra prisijungęs. Metodas post yra atsakingas už
     formos duomenų tvarkymą ir saugojimą. Jei formos duomenys yra teisingi, pranešimas
     "Congratulations! User Register Succesfully" yra rodomas vartotojui, jei ne - "Invalid Input Data".
      Paskutinė eilutė visada grąžina "app/customer_registration.html" šabloną su formos duomenimis."""

    def get(self, request):
        form = CustomerRegistrationForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, "app/customer_registration.html", locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Register Succesfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, "app/customer_registration.html", locals())


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    """Klasė ProfileView paveldi iš View klasės ir yra pritaikyta @method_decorator(login_required, name='dispatch')
    dekoratoriumi, reiškiančiu, kad vartotojas turi būti prisijungęs, kad galėtų matyti profilio informaciją.
    Metodas get yra atsakingas už profilio formos atvaizdavimą vartotojui ir tikrina, ar vartotojas yra prisijungęs.
     Metodas post yra atsakingas už profilio informacijos tvarkymą ir saugojimą. Jei formos duomenys yra teisingi,
     pranešimas "Congratulations! Profile Save Successfully" yra rodomas vartotojui, jei ne - "Invalid Input Data".
      Paskutinė eilutė visada grąžina "app/profile.html" šabloną su formos duomenimis."""

    def get(self, request):
        form = CustomerProfileForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/profile.html', locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            locality = form.cleaned_data['locality']
            zipcode = form.cleaned_data['zipcode']
            city = form.cleaned_data['city']

            reg = Customer(user=user, name=name, mobile=mobile, locality=locality, zipcode=zipcode, city=city)
            reg.save()
            messages.success(request, "Congratulations! Profile Save Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'app/profile.html', locals())


@login_required
def address(request):
    """funkcija naudoja @login_required dekoratorių, reiškiančią, kad vartotojas turi būti prisijungęs, kad galėtų
        matyti adreso informaciją. Funkcija vykdo kreipimąsi į duomenų bazę, kad gautų vartotojo adreso informaciją ir
        atvaizduoja "app/address.html" šabloną su gautais duomenimis ir informacija apie prisijungusio vartotojo
        krepšelio bei pageidavimų sąrašo elementų skaičių."""
    add = Customer.objects.filter(user=request.user)
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'app/address.html', locals())


@method_decorator(login_required, name='dispatch')
class updateAddress(View):
    """Ši klasė vadinama "updateAddress" ir ji yra skirta vartotojo adreso atnaujinimui. Ji turi "get" ir "post"
    metodus. "Get" metodas gauna vartotojo adreso duomenis iš duomenų bazės ir sukuria formą, kurią vartotojas gali
    pildyti ir pakeisti savo adresą. "Post" metodas gauna formos duomenis, patikrina juos, jei jie yra teisingi,
     atnaujina vartotojo adreso duomenis duomenų bazėje ir siunčia sėkmingo pranešimo vartotojui. Jei formos duomenys
      yra neteisingi, siunčiamas klaidos pranešimas. Abiejų metodų pradžioje yra "login_required" dekoratorius,
       kuris reikalauja, kad vartotojas būtų prisijungęs, kad galėtų pasiekti šią funkciją."""

    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/updateAddress.html', locals())

    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.mobile = form.cleaned_data['mobile']
            add.locality = form.cleaned_data['locality']
            add.zipcode = form.cleaned_data['zipcode']
            add.city = form.cleaned_data['city']
            add.save()

            messages.success(request, "Congratulations! Profile Save Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect("address")


@login_required
def add_to_cart(request):
    """funkcija, kuri leidžia vartotojui pridėti produktą į jų krepšelį. Vartotojas turi būti prisijungęs, kad
    galėtų naudotis šia funkcija. Funkcija naudoja "GET" metodą, kad gautų produkto ID iš URL ir tikrina, ar krepšelyje
     jau yra toks produktas. Jei yra, tai padidina jo kiekį, o jei ne, tai prideda produktą į krepšelį. Be to,
      funkcija taip pat apskaičiuoja bendrą krepšelio sumą ir grąžina vartotoją į produkto detalų puslapį."""
    user = request.user
    product_id = request.GET.get('prod_id')
    if Cart.objects.filter(product=product_id).exists():
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = round(amount + 3.50, 2)
        print(prod_id)
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return redirect('/product-detail/' + product_id)
    else:
        pass
        product = Product.objects.get(id=product_id)
        Cart(user=user, product=product).save()
        return redirect('/product-detail/' + product_id)


@login_required
def show_cart(request):
    """Ši funkcija reikalauja prisijungimo, kad galėtų būti naudojama. Tai nustato, kad vartotojas turi prisijungti
     prie sistemos, kad galėtų naudoti šią funkciją. Funkcija vadinama "show_cart" ir ji atvaizduoja vartotojo
     krepšelio turinį. Funkcija gauna visus vartotojo krepšelyje esančius produktus ir suskaičiuoja bendrą krepšelio
      kainą. Ji taip pat prideda 3.50 dolerių pristatymo kainą ir parodo bendrą sumą. Be to, ji taip pat skaičiuoja,
       kiek produktų yra vartotojo krepšelyje ir kiek produktų yra vartotojo norų sąraše. Galiausiai ji naudoja
       "locals" kintamuosius, kad perduotų informaciją į "addtocart.html" šabloną ir atvaizduoja jį vartotojui."""
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = round(amount + 3.50, 2)
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'app/addtocart.html', locals())


@login_required
def show_wishlist(request):
    """funkcija naudojama rodyti vartotojo pageidaujamų produktų sąrašą. Jos pradžioje patikrinama, ar vartotojas
    yra prisijungęs, ir jei taip, tai nustatomas krepšelio ir pageidaujamų produktų skaičius. Tada naudojama
    "Wishlist" objektų filtravimo funkcija, kad būtų gauti produktai, kuriuos vartotojas nori. Gauti produktai yra
     perduodami į "wishlist.html" šabloną, kur jie yra atvaizduojami vartotojui."""
    user = request.user
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    product = Wishlist.objects.filter(user=user)
    return render(request, "app/wishlist.html", locals())


@method_decorator(login_required, name='dispatch')
class checkout(View):
    """@method_decorator(login_required, name='dispatch') klase "checkout" reiškia, kad vartotojas turi būti
        prisijungęs, kad galėtų peržiūrėti šį puslapį. Metodas "get" naudojamas gauti informaciją iš serverio ir
        rodyti ją vartotojui. Metodas suskaičiuoja kiek elementų yra krepšelyje ir pageidavimų sąraše, kai vartotojas
         yra prisijungęs. Metodas taip pat gauna informaciją apie vartotojo adresą ir produktus, kuriuos jis turi savo
          krepšelyje. Jis taip pat apskaičiuoja bendrą sumą ir rodo ją vartotojui. Puslapis, kuriame informacija yra
          rodoma, yra "app/checkout.html"""
    def get(self, request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value
        totalamount = round(famount + 3.50, 2)
        return render(request, 'app/checkout.html', locals())


@login_required
def payment_done(request):
    """Ši funkcija yra skirta apmokėjimo patvirtinimui. Tai reiškia, kad kai vartotojas atlieka mokėjimą, jis bus
     nukreiptas į šią funkciją. Funkcija gauna informaciją apie užsakymo ID, mokėjimo ID ir kliento ID iš URL
     parametrų. Tada ji nustato, kad mokėjimas yra atliktas ir įrašo mokėjimo ID. Be to, ji sukuria naujus užsakymus
      pagal kiekvieną produktą, esantį krepšelyje, ir ištrina juos iš krepšelio. Galiausiai ji nukreipia vartotoją į
      užsakymų puslapį."""
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    cust_id = request.GET.get('cust_id')
    user = request.user
    customer = Customer.objects.get(id=cust_id)
    payment = Payment.objects.get(pay_order_id=order_id)
    payment.paid = True
    payment.pay_payment_id = payment_id
    payment.save()
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity, payment=payment).save()
        c.delete()
    return redirect("orders")


@login_required
def orders(request):
    """funkcija, kuri yra priskirta "orders" URL. Funkcija yra prieinama tik prisijungusiems vartotojams. Funkcija
    naudoja "OrderPlaced" modelį, kad gautų visus užsakymus, kuriuos padarė vartotojas. Tada funkcija naudoja "Cart"
     modelį, kad gautų krepšelio elementus ir "Wishlist" modelį, kad gautų pageidaujamų elementų skaičių. Galiausiai
     funkcija naudoja "render" funkciją, kad atvaizduotų "orders.html" šabloną su "order_placed" ir "totalitem" ir
      "wishitem" kintamaisiais."""
    order_placed = OrderPlaced.objects.filter(user=request.user)
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'app/orders.html', locals())


def plus_cart(request):
    """funkcija, kuri reaguoja į "plus" mygtuko paspaudimą krepšelio puslapyje. Funkcija naudoja GET metodą, kad
    gautų produkto ID iš lankytojo. Tada ji naudoja tai, kad gauti objektą Cart klasės, kuris atitinka produktą ir
     lankytoją. Tada ji padidina kiekį vienetais, ir išsaugo objektą. Tada ji suskaičiuoja bendrą kiekį ir bendrą
      kainą krepšelio produktų. Galiausiai ji sukuria duomenų aibę, kurioje yra kiekis, suma ir bendra suma, ir
      siunčia ją atgal kaip JSON atsakymas."""
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = round(amount + 3.50, 2)
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)


def minus_cart(request):
    """funkcija yra skirta krepšelio produktų kiekio sumažinimui. Jei vartotojas paspaudžia "minus" mygtuką,
    funkcija gauna produkto ID iš GET užklausos ir naudoja jį Cart objektų paieškai su vartotoju susietam produktui.
     Jei produktų kiekis yra didesnis nei 1, kiekis sumažinamas vienu ir išsaugomas. Jei produktų kiekis yra 1,
     nieko nevykdoma. Tuomet funkcija naudoja vartotoją ir krepšelio produktus, kad suskaičiuotų bendrą produktų
     kainą ir bendrą kainą su pristatymu, ir siunčia atgal JSON duomenis apie produktų kiekį, bendrą produktų kainą
      ir bendrą kainą su pristatymu."""
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        if c.quantity > 1:
            c.quantity -= 1
            c.save()
        else:
            pass
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
            totalamount = round(amount + 3.50, 2)
            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount': totalamount
            }
            return JsonResponse(data)


def remove_cart(request):
    """funkcija yra skirta krepšelio produktų pašalinimui. Jei vartotojas paspaudžia "Pašalinti iš krepšelio" mygtuką,
     funkcija gauna produkto ID naudojant GET metodą. Tada naudoja tai ID, kad pašalintų atitinkamą produktą iš
     krepšelio, esančio duomenų bazėje. Po to, funkcija suskaičiuoja bendrą krepšelio kainą ir grąžina rezultatus
      JSON formate, kad jie būtų atvaizduoti vartotojui sąsajoje."""
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = round(amount + 3.50, 2)
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)


def plus_wishlist(request):
    """funkcija yra skirta pridėti produktus į "pageidavimų sąrašą". Jei vartotojas yra prisijungęs ir paspaudžia
    "pageidavimų sąrašo" mygtuką, funkcija gaunama produkto ID ir produktą iš duomenų bazės pagal šį ID. Tada
    funkcija sukuria naują įrašą vartotojo ir produkto "pageidavimų sąraše". Vartotojas gauna pranešimą, kad
     produktas buvo sėkmingai pridėtas į "pageidavimų sąrašą"."""
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist.objects.get_or_create(user=user, product=product)
        data = {
            'message': 'Wishlist Added Successfully',
        }
        return JsonResponse(data)


def minus_wishlist(request):
    """Funkcija "minus_wishlist" yra atsakinga už produkto pašalinimą iš vartotojo norų sąrašo. Jei vartotojas
    paspaudžia "minus" mygtuką vienam produktui, funkcija gauna produkto ID, nustato produktą pagal jo ID ir
     vartotoją, kuris nori pašalinti produktą iš savo norų sąrašo. Tada funkcija pašalina produktą iš norų sąrašo
     ir siunčia atgal "sėkmingai pašalinta" žinutę."""
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist.objects.filter(user=user, product=product).delete()
        data = {
            'message': 'Wishlist Remove Successfully',
        }
        return JsonResponse(data)


@login_required
def search(request):
    """Ši funkcija yra skirta vartotojo paieškai produktų sistemoje. Vartotojas gali įvesti paieškos užklausą ir
    sistema atvaizduos produktus, kurių pavadinimuose yra įvesta užklausa. Jei vartotojas yra prisijungęs, tai
     taip pat bus atvaizduojama kiekvieno produkto krepšelio ir pageidavimų sąrašo elementų kiekis. Rezultatai bus
     atvaizduojami "app/search.html" šablono puslapyje."""
    query = request.GET['search']
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    product = Product.objects.filter(Q(title__icontains=query))
    return render(request, "app/search.html", locals())
