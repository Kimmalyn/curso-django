# Corey schafer, youtuber de python buenardo

""" para correr el el server tengo que escribir en la consola "Python manage.py runserver"
    hay que estar ubicado en la carpeta del projecto
"""

# aca importo librerias que uso
import datetime
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.template.loader import get_template
from django.shortcuts import render


class Persona:  # clase que cree para probar cosas
    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad


def tu_vieja(request):  # tu_vieja es el nombre de la vista

    p1 = Persona("Levi", 20)

    temitas = ["plantillas", "modelos", "formulario", "vistas", "despliegue"]

    fecha_actual = datetime.datetime.now()

    # esta forma de cargar es poco optima la buena son los loaders

    """ plantilla = open("C:/Users/lucas/OneDrive/Escritorio/django/plantillas/texto.html")

    plt = Template(plantilla.read())  # objeto platilla que lee el template de la misma

    plantilla.close() """

    """ctx = Context(
        {
            "nombre_persona": p1.nombre,
            "edad_persona": p1.edad,
            "fecha": fecha_actual,
            "temas": temitas,
        }
    )  # contexto donde paso mis variables para usarlas en la plantilla
    # no see puede pasar con context como parametro si uso loaders """

    """ plt = get_template('texto.html') #asi es la forma mas optima, con loaders

    doc = plt.render(
        {
            "nombre_persona": p1.nombre,
            "edad_persona": p1.edad,
            "fecha": fecha_actual,
            "temas": temitas,
        }
    )  
    # objeto que guarda el render, aca pongo objetos que puedo usar en el template, paso del dict directamente

    #return HttpResponse(doc)  # me genera la vista retornando el doc """

    return render(
        request,
        "texto.html",
        {
            "nombre_persona": p1.nombre,
            "edad_persona": p1.edad,
            "fecha": fecha_actual,
            "temas": temitas,
        },
    )  # al importar los shortcuts puedo hacer esto


def fechita(request):  # aca practique mostrar cosas dinamicas (se actualizan)

    fechahoy = datetime.datetime.now()

    texto = (
        """
    <html>
        <body>
        <h1>
        fecha y hora actuales %s
        </h1>
        </body>
        </html>"""
        % fechahoy
    )  # si no uso una plantilla el texto lo hago directamente en la variable, esta tambien esta mal

    return HttpResponse(texto)


def calcular_edad(
    request, year, edad
):  # aca practique mezclar cosas dinamicas, los date, con estaticas, la fecha de naciemiento

    period = year - 2020
    edadfutura = edad + period
    texto = "<html><body><h2> en año %s tendras %s <h2><body><h2>" % (year, edadfutura)
    return HttpResponse(texto)


def hija(request):# aca creo  la vista del templatte "hija"


    fecha = datetime.datetime.now()

    return render(request, "hija.html", {"fechita": fecha})


# name = input("puteame dale: ")
# print("tu vieja")

