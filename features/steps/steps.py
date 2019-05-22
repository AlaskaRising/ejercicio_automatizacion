from behave import *
from pares import *

from behave import register_type
from hamcrest import assert_that, equal_to


def parse_number(text):
    """
    Convert parsed text into a number.
    :param text: Parsed text, called by :py:meth:`parse.Parser.parse()`.
    :return: Number instance (integer), created from parsed text.
    """
    return int(text)


# -- REGISTER: User-defined type converter (parse_type).
register_type(Number=parse_number)


@given('un numero')
def step_impl(context):
    context.numeros = Numeros()


@when('reciba "{numero:Number}"')
def step_impl(context, numero):
    #assert isinstance(numero, int)
    context.numeros.saber_si_es_par(numero)


@then('la funcion dice si es "{par:Number}"')
def step_impl(context, par):
    #assert isinstance(expected, bool)
    assert_that(context.numeros.numeros_pares, equal_to(par))
