from django.apps import AppConfig


class AppConfig(AppConfig):
    """yra Django programos konfigūravimo klasė. Jos tikslas yra nustatyti programos konfigūravimo parametrus, kurie
    bus naudojami visame projekte. Konkrečiai, ši klasė nustato "default_auto_field" parametro reikšmę į
    "django.db.models.BigAutoField", kas reiškia, kad automatiškai sugeneruojami ID laukai bus didesni nei
    standartiniai. Taip pat klasė nustato programos pavadinimą kaip "app"."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
