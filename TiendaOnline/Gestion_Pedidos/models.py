from django.db import models

# Create your models here.

""" Comandos para crear una app: 
    python manage.py startapp 'nombre app'
    no olvidar agregar app en settings.py del proyecto"""


class Clientes(models.Model):

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField
    tfno = models.CharField(max_length=10)



class Articulos(models.Model):

    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return "EL nombre es %s la seccion es %s y el precio es %s " %(self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):

    nro_pedido = models.IntegerField()
    fecha = models.DateTimeField()
    entregado = models.BooleanField()


"""------------comandos para cargar tablas---------------
    para migrar y crear la db y sus tablas debemos hacer lo siguiente
   1- python manage.py makemigrations
   2- python manage.py sqlmigrate Gestion_Pedidos 0001 // genera el codigo sql see puede evitar
   (el 0001 es el numero de la migracion se genera cuando haces el makee migration)
    BEGIN;
    --    
    -- Create model Articulos
    --
    CREATE TABLE "Gestion_Pedidos_articulos" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "nombre" varchar(30) NOT NULL, 
    "seccion" varchar(30) NOT NULL, 
    "precio" integer NOT NULL);
    --
    -- Create model Clientes
    --
    CREATE TABLE "Gestion_Pedidos_clientes" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "nombre" varchar(30) NOT NULL, 
    "direccion" varchar(50) NOT NULL, 
    "tfno" varchar(10) NOT NULL);
    --
    -- Create model Pedidos
    --
    CREATE TABLE "Gestion_Pedidos_pedidos" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "nro_pedido" integer NOT NULL, 
    "fecha" datetime NOT NULL, 
    "entregado" bool NOT NULL);

    COMMIT;

    3- python manage.py migrate"""

"""------------cargar y guardar articulo---------------

    python manage.py shell

    from Gestion_Pedidos.models import Articulos
    art=Articulos(nombre='Volt', seccion='subfusiles', precio=90) 
    art.save()"""

""" ------------updatear articulo---------------
    art.propiedad = nuevo valor
    art.save()"""

"""------------eliminar articulo---------------
    art=Articulos.objects.get(id=1)
    art.Delete()
    """

"""------------consultas--------------- 
    lista=Articulos.objects.all()

    lista.query.__str__()=

    SELECT "Gestion_Pedidos_articulos"."id", "Gestion_Pedidos_articulos"."nombre", "Gestion_Pedidos_articulos"."seccion", "Gestion_Pedidos_articulos"."precio" 
    FROM "Gestion_Pedidos_articulos

    Articulos(nombre='Volt', seccion='subfusiles', precio=90) 

    Articulos.objects.filter(seccion='fusiles', precio__gte = 80) (>)

    Articulos.objects.filter(precio__gte = 90).order_by('precio')"""