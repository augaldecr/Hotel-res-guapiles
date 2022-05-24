# -*- encoding: utf-8 -*-
from django.db import models


class Hotel(models.Model):

    nombreComercial = models.CharField('Nombre comercial', max_length=50)
    nombreLegal = models.CharField('Nombre legal', max_length=50)
    cedJuridica = models.CharField('Cedula jurídica', max_length=15)
    direccion = models.CharField('Dirección', max_length=150)
    ImpuestoDeVentas = models.PositiveSmallIntegerField('Impuesto de ventas')

    class Meta:
        verbose_name = "hotel"
        verbose_name_plural = "hoteles"

    def __str__(self):
        return u"%s" %self.nombreComercial
    

class Habitacion(models.Model):

    numero = models.PositiveSmallIntegerField('Número')
    localizacion = models.CharField('Localización', max_length=50)
    precioBase = models.PositiveSmallIntegerField('Precio base')
    hotel = models.ForeignKey('Hotel')

    class Meta:
        verbose_name = "habitación"
        verbose_name_plural = "habitaciones"

    def __str__(self):
        return u"%i" %self.numero


class Persona(models.Model):

    correo = models.EmailField()
    nombre = models.CharField(max_length=25)
    apellido1 = models.CharField(max_length=25, blank=True)
    apellido2 = models.CharField(max_length=25, blank=True)
    telefono = models.CharField(max_length=15)

    class Meta:
        verbose_name = "persona"
        verbose_name_plural = "personas"

    def __str__(self):
        return u"%s %s %s"%(self.apellido1, self.apellido2, self.nombre)


class Extra(models.Model):

    nombre = models.CharField(max_length=25)
    precio = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "cargo extra"
        verbose_name_plural = "cargos extras"

    def __str__(self):
        return u"%s"%self.nombre
    

# class Consumo(models.Model):

#     fecha = models.DateField('Fecha', auto_now=False, auto_now_add=False)
#     habitacion = models.ForeignKey('Habitacion')
#     persona = models.ForeignKey('Persona')
#     extras = models.ManyToManyField('Extra')
#     facturada = models.BooleanField(default=False)

#     class Meta:
#         verbose_name = "reservación"
#         verbose_name_plural = "reservaciones"

#     def fechita(self):
#         return u"%s/%s/%s"%(self.fecha.day, self.fecha.month,self.fecha.year)

#     def __str__(self):
#         return u"%s - %s - %s"%(self.fechita(), self.persona, self.habitacion)


class Proveedor(models.Model):

    cedula = models.CharField('Cédula', max_length=25)
    persona = models.ForeignKey('Persona')

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return u"%s - %s"%(self.cedula, cedula.persona)


class Producto(models.Model):

    nombre = models.CharField(max_length=65)
    costo = models.FloatField()
    porc_util = models.PositiveSmallIntegerField()
    precio = models.FloatField()
    proveedor = models.ForeignKey('Proveedor', blank=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return u"%s"%self.nombre


class Factura(models.Model):

    fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    cliente = models.ForeignKey('Persona')
    subtotal = models.SmallIntegerField()
    iv = models.FloatField('I.V.')
    total = models.FloatField()

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"

    def fechita(self):
        return u"%s/%s/%s %s:%s:%s"%(self.fecha.day, self.fecha.month,self.fecha.year, self.fecha.hour, self.fecha.minutes, self.fecha.seconds)

    def __str__(self):
        return u"Factura %s - %s - %s" %(self.id, self.fechita(), self.cliente)


class Registro(models.Model):

    cantidad = models.PositiveSmallIntegerField()
    producto = models.ForeignKey('Producto')
    factura = models.ForeignKey('Factura')

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

    def __str__(self):
        return u"%s %s"%(self.cantidad, self.producto)