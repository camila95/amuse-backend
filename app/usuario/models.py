# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Persona(models.Model):
    TIPO_PROSPECTO = 0
    TIPO_APRENDIZ = 1
    TIPO_DIRECTOR = 2
    TIPO_CHOICES = (
        (TIPO_PROSPECTO, 'Prospecto'),
        (TIPO_APRENDIZ, 'Aprendiz'),
        (TIPO_DIRECTOR, 'Director'),
    )
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateTimeField()
    usuario = models.ForeignKey(User)
    rh = models.CharField(max_length=5)
    eps = models.CharField(max_length=255)
    tipo = models.SmallIntegerField(choices=TIPO_CHOICES,
        default=TIPO_PROSPECTO)
    direccion = models.CharField(max_length=500)
    acudientes = models.ManyToManyField('usuario.Acudiente')


    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return self.get_nombre_completo()

    def get_nombre_completo(self):
        return '%s %s' % (self.nombre, self.apellido)


class Acudiente(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)

    def __str__(self):
        return self.get_nombre_completo()

    def get_nombre_completo(self):
        return '%s %s' % (self.nombre, self.apellido)


class Telefono(models.Model):
    TIPO_FIJO = 0
    TIPO_MOVIL = 1
    TIPO_CHOICES = (
        (TIPO_FIJO, 'Télefono fijo'),
        (TIPO_MOVIL, 'Télefono móvil')
    )
    persona = models.ForeignKey('usuario.Persona')
    numero = models.CharField(max_length=255)
    tipo = models.SmallIntegerField(choices=TIPO_CHOICES, default=TIPO_MOVIL)

    def __str__(self):
        return '%s (%s)' % (self.numero, self.get_tipo_display())
