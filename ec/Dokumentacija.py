
###################################--Sistemos dokumentacija--####################################################
"""Projekto aprašymas:

Šis projektas yra e-commerce platforma, skirta elektroniniams produktams parduoti. Vartotojai galės užsiregistruoti,
 kurti savo paskyras, peržiūrėti ir užsakyti produktus. Administratorius turės galimybę valdyti produktų sąrašus ir
  užsakymų sąrašus."""

###################################--Tikslas--###################################################################
"""Tikslas
Tikslas yra sukurti patogų ir funkcionalų e-commerce platformą, kurioje vartotojai galėtų patogiai ir 
saugiai atlikti savo pirkimus."""

###################################--Funkcionalumas--###########################################################
"""Funkcionalumas
Sistema turi šias funkcijas:
-Vartotojo prisijungimas ir registracija
-Produktų peržiūra ir užsakymas
-Užsakymų valdymas ir peržiūra (patvirtinimas, atšaukimas ir kt.)
-Mokėjimo valdymas 
-Vartotojo profilio redagavimas ir mokėjimo informacijos valdymas
-Administratoriaus vartotojų valdymas ir produktų valdymas"""

"""Vartotojo funkcionalumas
Vartotojas gali:
-Peržiūrėti produktų sąrašą
-Užsisakyti produktus
-Peržiūrėti užsakytų produktų sąrašą
-Peržiūrėti užsakymo būseną
-Atlikti mokėjimą už užsakytus produktus
-Redaguoti savo profilį ir mokėjimo informaciją"""

"""Administratoriaus funkcionalumas
Administratorius gali:
-Valdyti vartotojų sąrašą
-Valdyti produktų sąrašą
-Valdyti užsakymų sąrašą
-Patvirtinti užsakymus
-Atšaukti užsakymus
-Redaguoti užsakymų būseną
-Redaguoti produktų ir vartotojų informaciją"""

###################################--Įgyvendinimas--#############################################################
"""Įgyvendinimas
Sistema įgyvendinta naudojant Python programavimo kalbą ir Django framework."""

###################################--Projekto struktūra--########################################################
"""
Projekto kodas yra suskirstytas į kelis failus ir aplankalus:

app aplankalas yra pagrindinis aplankalas, kuriame yra visi projekto modeliai, formos ir atvaizdavimo šablonai.

models.py faile yra visi projekto modeliai: User, Customer, Product, OrderPlaced, Payment.
forms.py faile yra visi projekto formos: OrderForm, PaymentForm.
views.py faile yra visi projekto atvaizdavimo metodai.
templates aplankalas yra skirtas šablonų failams.

static aplankalas yra skirtas estetiniams failams, tokiems kaip CSS ir JavaScript failai, bei paveikslėliai.

css aplankalas yra skirtas visoms projekto CSS failams: all.min.css, owl.carousel.min.css, style.css.
images aplankalas yra skirtas visoms projekto paveikslėlių failams: banner, product.
js aplankalas yra skirtas visoms projekto JavaScript failams: all.min.js, myscript.js, owl.carousel.min.js."""

###################################--Modeliai--###################################################################
"""Modeliai
Sistemoje yra keli modeliai: Vartotojas, Klientas, Produktas, Užsakymas ir Mokėjimas.

1.Vartotojas modelis aprašo sistemos vartotojus, kuriuos galima redaguoti ir valdyti administratoriaus sąsajoje.
2.Kliento modelis aprašo klientus, kurie gali užsisakyti produktus.
3.Produkto modelis aprašo produktus, kurie yra parduodami sistemoje.
4.Užsakymo modelis aprašo užsakymus, kuriuos vartotojas padarė. 
Jame yra laukai:
vartotojas, klientas, produktas, kiekis, užsakymo data, būsena ir mokėjimas.
Mokėjimo modelis aprašo mokėjimus, kuriuos vartotojas atliko užsakant produktus."""

###################################--Administratoriaus registracija--##############################################
"""Administratoriaus registracija
Sistemoje yra administratoriaus registracijos klasė Užsakymų modeliui, kuri parodo administratoriaus sąsajoje, kokie
laukai bus rodomi užsakymo sąraše (id, vartotojas, klientas, produktai, kiekis, užsakymo data, būsena, mokėjimai).
Be to, tai taip pat nurodo, kaip bus rodomas kiekvieno produkto ir mokėjimo pavadinimas administratoriaus sąsajoje
(kaip nuoroda į produkto ar mokėjimo redagavimo puslapį)."""

###################################--Klaidų valdymas--##########################################################
"""Klaidų valdymas
Sistema turi integruotą klaidų valdymo sistemą, kuri nustato ir praneša apie bet kokias klaidas, kurios atsirado dėl 
techninių problemų ar neteisingo naudojimo. Šios klaidos gali būti išsprendžiamos administratoriaus sąsajoje."""

###################################--Saugumas--#################################################################
"""Saugumas
Sistema yra suderinta su keletu saugumo funkcijų, kad apsaugotų vartotojų duomenis ir užtikrintų saugų produktų 
užsakymų procesą. Tai apima vartotojų slaptažodžių šifravimą, SSL šifravimo protokolą ir reguliarias saugos 
atnaujinimus."""

###################################--Mokėjimo sistema--#########################################################
"""Mokėjimo sistema
Sistemoje naudojama trečiosios šalies mokėjimo sistema, kuri užtikrina saugų ir patikimą mokėjimų atlikimą.
Vartotojas gali atlikti mokėjimą naudodamas kreditinę kortelę arba kitus prieinamus mokėjimo būdus."""

###################################--Problematikos ir sprendimai--#########################################################
"""Problematikos ir sprendimai:

1.Duomenų integracijos problema: Sistemoje turėjou sujungti kelis modelius, tokius kaip vartotojas, klientas, 
produktas ir mokėjimas. Tai reikalavo atidžiai planuoti duomenų bazės struktūrą ir nustatyti, kaip informacija tarp 
jų bus perduodama. Sprendimas buvo naudoti ForeignKey sąryšius tarp modelių, kad būtų išsaugoma sąsaja tarp jų.

2.Autentifikavimo ir autorizavimo problema: Reikėjo nustatyti, kurie vartotojai turi teisę matyti ir redaguoti 
informaciją sistemoje. Sprendimas buvo naudoti Django autentifikavimo ir autorizavimo sistemas, kad būtų galima 
nustatyti, kurie vartotojai turi teisę matyti ir redaguoti informaciją.

3.Duomenų atvaizdavimo problema: Reikėjo sukurti interfeisą, kuris leistų vartotojams greitai ir lengvai matyti ir 
redaguoti informaciją sistemoje. Sprendimas buvo naudoti Django modelių ir formų bibliotekas, kad būtų galima 
automatiškai generuoti formas ir lenteles, skirtas redaguoti ir atvaizduoti informaciją.

4.Duomenų saugumo problema: Reikėjo užtikrinti, kad duomenys būtų saugiai saugomi ir apsaugoti nuo neteisėto patekimo. 
Sprendimas buvo naudoti HTTPS ir apsaugoti duomenų bazę šifravimo technologijomis.

5.Pagal šiuos sprendimus buvo įgyvendinta veiksminga ir saugi sistema, kuri leidžia vartotojams efektyviai valdyti 
ir peržiūrėti informaciją."""

###################################--Galimybės tobulinti sistemą--#########################################################
"""Galimybės tobulinti sistemą:

1.Integravimas su socialiniais tinklais: šiuo metu sistema leidžia vartotojams prisiregistruoti ir prisijungti 
naudojantis savo el. paštu ir slaptažodžiu. Tačiau būtų galima įtraukti galimybę prisijungti ir per socialinius 
tinklus, tokius kaip Facebook ar Google.

2.Pridėti mokėjimo būdų: tokių kaip kreditinės kortelės ar banko pavedimai, taip pat galima prijungti paypal ar kitą 
sistemą.

3.Lengvesnis produktų pridėjimas: šiuo metu administratorius turi rankiniu būdu pridėti produktus į sistemą. 
Būtų naudinga įvesti galimybę importuoti produktų duomenis iš CSV failo.

4.Produktų kategorijos: šiuo metu produktai nėra suskirstyti į kategorijas, todėl vartotojai turi paieškoti 
produktų per visą produktų sąrašą. Būtų patogu vartotojams, jei produktai būtų suskirstyti per filtravimą.

5.Produktų atsiliepimai ir reitingai: šiuo metu sistema neturi galimybės vartotojams rašyti atsiliepimus apie 
produktus ir juos reitinguoti. Tai padėtų vartotojams lengviau pasirinkti produktus ir sužinoti kitų vartotojų nuomonę.
"""