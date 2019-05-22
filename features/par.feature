Feature: La funcion par para la app de pares
Scenario Outline: Revisar numeros
  Given un numero
  When reciba "<numero>"
  Then la funcion dice si es "<par>"

  Examples: Numeros
  | numero        | par |
  | 2             | 1   |
  | 4             | 1   |
