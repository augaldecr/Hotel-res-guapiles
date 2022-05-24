# -*- encoding: utf-8 -*-
from django.db import models
# from administracion.models import Habitacion, Persona, Extra

# class Reservacion(models.Model):

#     fecha = models.DateField('Fecha', auto_now=False, auto_now_add=False)
#     habitacion = models.ForeignKey('Habitacion')
#     persona = models.ForeignKey('Persona')
#     extras = models.ManyToManyField('Extra')
#     aprobada = models.BooleanField(default=False)
#     facturada = models.BooleanField(default=False)

#     class Meta:
#         verbose_name = "reservación"
#         verbose_name_plural = "reservaciones"

#     def fechita(self):
#         return u"%s/%s/%s"%(self.fecha.day, self.fecha.month,self.fecha.year)

#    def __str__(self):
#        return u"%s - %s - %s"%(self.fechita(), self.persona, self.habitacion)