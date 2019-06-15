# Linea de automatización de desarrollo de software
## Universidad Distrital Francisco José de Caldas :books:
Ejercicio de automatización para el desarrollo de un producto de software


Todos los proyectos alojados en este repositorio han sido elaborados por :
- Miguel Angel Vega Alonso @Miavega
- Nicolas Steeven Rivera 
- María Camila Guerrero Giraldo

### Producto

Se realiza un programa en Python que valide si un número es par . Recibe un parámetro de tipo int (Entero) y retorna un número entero 1 o 0 , que indica que es par y que no es par respectivamente .
![Programa que valida si un número es par](https://github.com/AlaskaRising/ejercicio_automatizacion/blob/master/carbon.png)

## Herramienta para Automatizar las Pruebas

Behave es un framework de BDD . Es decir Behavior Driven Development, o sea, desarrollo dirigido por comportamiento. Como bien lo indica su nombre, no se trata de una técnica de testing, sino que es una estrategia de desarrollo (así como TDD, que es test driven development). Lo que plantea es definir un lenguaje común para el negocio y para los técnicos, y utilizar eso como parte inicial del desarrollo y el testing. Por esto es que es importante que vos como tester entiendas bien qué es BDD.

![Pasos que sigue para testear](https://github.com/AlaskaRising/ejercicio_automatizacion/blob/master/carbon1.png)
![Ejemplos](https://github.com/AlaskaRising/ejercicio_automatizacion/blob/master/carbon2.png)
## Ejecución

1. Es importante tener instalado Behave. Si no lo tiene instalado corra 

```console
pip install behave
```

2. Situese en la carpeta del proyecto 

3. Ejecute el comando

```console
behave
```
4. A continuación verá los resultados de las pruebas automatizadas con BDD .

![Resultados Test](https://github.com/AlaskaRising/ejercicio_automatizacion/blob/master/resultado.PNG)

## Docker
### Pre-requisitos 📋

_Cosas necesarias para instalar el software y como instalarlas_

```
Docker versión 3.3
```

### Instalación 🔧

_Construir la imagen de Docker Compose_

```
docker-compose build
```

_Subir el Docker Compose_

```
docker-compose up
```

_El servidor se ejecuta en el puerto 8080_
_http://localhost:8080/_

## Resultados
_Al crear la tarea y enlazarla al [repositorio](https://github.com/AlaskaRising/ejercicio_automatizacion) los resultados son:_

![Resultados Test Valido](https://github.com/AlaskaRising/ejercicio_automatizacion/blob/master/jenkins1.PNG)
![Resultados Test Valido Completo](https://github.com/AlaskaRising/ejercicio_automatizacion/blob/master/jenkins2.PNG)
![Resultados Test Fallido](https://github.com/AlaskaRising/ejercicio_automatizacion/blob/master/jenkins3.PNG)

## Construido con 🛠️

_Herramientas_

* [Behave](https://behave.readthedocs.io/en/latest/) - Utiliza pruebas escritas en lenguaje natural, respaldadas por código Python.
* [Unittest](https://docs.python.org/3/library/unittest.html) - Framework de pruebas unitarias en Python.
* [Jenkins](https://jenkins.io/) - Jenkins es un servidor de automatización open source escrito en Java.
