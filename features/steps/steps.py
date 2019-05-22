from behave import *
from pares import *

@given('una funcion')
def step_impl(context):
    context.numeros = Numeros()

@when('reciba numero')
def step_impl(context, number):
    context.numeros.saber_si_es_par(number)

@then('la funcion dice si es par')
def step_impl(context):
    assert (context.numeros.saber_si_es_par == True)