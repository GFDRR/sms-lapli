__author__ = 'jbjeanniton'

from django.core.validators import RegexValidator

regex_tel = RegexValidator(
    regex="^509[0-9]{8}$",
    message="La valeur ne correspond pas au format d'un numero de telephone",
)

regex_noid = RegexValidator(
    regex='^[0-9]{3}-[0-9]{3}-[0-9]{3}-[0-9]{1}$|^\d{2}-\d{2}-\d{2}-\d{4}-\d{2}-\d{5}$',
    message="La valeur ne correspond ni au formt d'un code CIN ni a celui d'un NIF",
)

regex_percent = RegexValidator(
    regex='^[1-9][0-9]?$|^100$|^0$',
    message="Saisissez un nombre entre 0 et 100",
)


