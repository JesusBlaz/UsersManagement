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
