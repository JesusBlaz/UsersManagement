## Python
import re

## Apps terceros
from curp import CURP, CURPValueError

## Django
from django.core.exceptions import ValidationError


# CURP
def curp_validation(value):
    """ Función que valida un curp """

    curp_validada = CURP(value)
    if not curp_validada:
        raise CURPValueError


# RFC
rfc_pattern_pf = "^(([A-ZÑ&]{4})([0-9]{2})([0][13578]|[1][02])(([0][1-9]|[12][\\d])|[3][01])([A-Z0-9]{3}))|(([A-ZÑ&]{4})([0-9]{2})([0][13456789]|[1][012])(([0][1-9]|[12][\\d])|[3][0])([A-Z0-9]{3}))|(([A-ZÑ&]{4})([02468][048]|[13579][26])[0][2]([0][1-9]|[12][\\d])([A-Z0-9]{3}))|(([A-ZÑ&]{4})([0-9]{2})[0][2]([0][1-9]|[1][0-9]|[2][0-8])([A-Z0-9]{3}))$"

def rfc_validation(value):
    """ Función que valida el RFC (Expresión regular) """

    compilar = re.compile(rfc_pattern_pf)
    comparar = compilar.match(value)
    if comparar is None:
        raise ValidationError('RFC incorrecto')


