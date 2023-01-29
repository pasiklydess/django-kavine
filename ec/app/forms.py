from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm,\
    SetPasswordForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import Customer


class LoginForm(AuthenticationForm):
    """"LoginForm" yra specialus formos tipas, kuris yra naudojamas prisijungimo proceso metu. Tai paveldi
    iš "AuthenticationForm" klasės, kuri yra Django nusistatymų dalis. Formoje yra du laukai: "username" ir "password",
     kurie yra būtini prisijungimo procese. "username" laukas yra "UsernameField" tipo, o "password" laukas yra
     "CharField" tipo. Abiem laukams yra priskirti specialūs atributai, kurie padeda HTML žiniatinklyje atvaizduoti
     laukų išvaizdą."""
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                                                 'class': 'form-control'}))


class CustomerRegistrationForm(UserCreationForm):
    """"CustomerRegistrationForm" yra Django formos klasė, kuri naudoja "UserCreationForm" pagrindą. Tai reiškia, kad
     ji turi standartinius laukus, reikalingus vartotojo registracijai, tokius kaip vartotojo vardas, elektroninio
     pašto adresas ir slaptažodis. Šioje formoje taip pat yra papildomi laukai, kurie yra reikalingi "Customer"
     modeliui, tačiau jie nėra reikalingi standartiniam vartotojo modeliui. Formos laukai yra atributų klasės, kurios
      nustato, kaip laukai bus atvaizduojami HTML puslapyje."""
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MyPasswordChangeForm(PasswordChangeForm):
    """Kodas apibūdina tris skirtingas formas, kurias gali naudoti vartotojas svetainėje: LoginForm yra prisijungimo
    forma, kurioje vartotojas įveda savo vardą ar el. pašto adresą ir slaptažodį. CustomerRegistrationForm yra
    registracijos forma, kurioje vartotojas įveda savo vardą, el. pašto adresą, slaptažodį ir patvirtina slaptažodį.
    MyPasswordChangeForm yra slaptažodžio keitimo forma, kurioje vartotojas įveda seną slaptažodį, naują slaptažodį
    ir patvirtina naują slaptažodį. Formos taip pat turi CSS klasės, kurios leidžia jas išvaizdžiai atvaizduoti
    svetainėje."""
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs=
        {'autofocus': 'True', 'autocomplete': 'current-password', 'class': 'form-control'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs=
        {'autocomplete': 'current-password', 'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs=
        {'autocomplete': 'current-password', 'class': 'form-control'}))


class MyPasswordResetForm(PasswordResetForm):
    """klasė, kuri paveldi iš Django "PasswordResetForm" klasės. Tai yra forma, kuri naudojama slaptažodžio atstatymui.
     Formoje yra tik vienas laukas - el. pašto laukas, kuris yra "email" ir jo widget yra "forms.EmailInput" su
     atributais "class: 'form-control'" - tai reiškia, kad laukas bus atvaizduojamas kaip HTML formos laukas su
     "form-control" klasės CSS stiliumi. Forma naudojama kai vartotojas nori atstatyti savo slaptažodį."""
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))



class MySetPasswordForm(SetPasswordForm):
    """klasė, kuri naudojama nustatant naują slaptažodį vartotojui. Ji paveldi iš SetPasswordForm klasės ir turi
    laukus new_password1 ir new_password2, kurie yra reikalingi vartotojui nustatyti naują slaptažodį ir patvirtinti
    jį. Formos laukai yra nustatyti su atributais, tokiais kaip 'autocomplete': 'current-password' ir 'class':
    'form-control', kurie nustato lauko išvaizdą ir funkcionalumą."""
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs=
        {'autocomplete': 'current-password', 'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs=
        {'autocomplete': 'current-password', 'class': 'form-control'}))


class CustomerProfileForm(forms.ModelForm):
    """klasė, kuri naudoja "Customer" modelio laukus, kad sukurtų formą vartotojo profilio informacijos atnaujinimui.
     Formos laukai yra "name", "mobile", "locality", "zipcode" ir "city". Kiekvienam laukui priskiriamas "form-control"
      CSS klasės atributas, kuris nustato formos stilių."""
    class Meta:
        model = Customer
        fields = ['name', 'mobile', 'locality', 'zipcode', 'city']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }
