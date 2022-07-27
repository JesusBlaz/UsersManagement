## Python
import re

## Apps terceros
from curp import CURP, CURPValueError

## Django
from django.core.exceptions import ValidationError


# CURP
def curp_validation(value):
    """ Función que valida un curp """

    curp_validada = "^[A-Z]{1}[AEIOU]{1}[A-Z]{2}[0-9]{2}(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[HM]{1}(AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)[B-DF-HJ-NP-TV-Z]{3}[0-9A-Z]{1}[0-9]{1}$"

    compilar = re.compile(curp_validada)
    comparar = compilar.match(value)
    if comparar is None:
        raise ValidationError('CURP incorrecto')


# RFC
def rfc_validation(value):
    """ Función que valida el RFC (Expresión regular) """

    rfc_pattern_pf = "^(([A-ZÑ&]{4})([0-9]{2})([0][13578]|[1][02])(([0][1-9]|[12][\\d])|[3][01])([A-Z0-9]{3}))|(([A-ZÑ&]{4})([0-9]{2})([0][13456789]|[1][012])(([0][1-9]|[12][\\d])|[3][0])([A-Z0-9]{3}))|(([A-ZÑ&]{4})([02468][048]|[13579][26])[0][2]([0][1-9]|[12][\\d])([A-Z0-9]{3}))|(([A-ZÑ&]{4})([0-9]{2})[0][2]([0][1-9]|[1][0-9]|[2][0-8])([A-Z0-9]{3}))$"

    compilar = re.compile(rfc_pattern_pf)
    comparar = compilar.match(value)
    if comparar is None:
        raise ValidationError('RFC incorrecto')


# CP
def cp_validation(value):
    """ Función que valida el Código postal """

    cp_regex = "[0-9]{5}"

    compilar = re.compile(cp_regex)
    comparar = compilar.match(value)
    if comparar is None:
        raise ValidationError('CP incorrecto')

