import os

from django.conf import settings
from django.db import models


class BaseManager(models.Manager):

    def activos(self):
        return self.filter(activo=True)


class Base(models.Model):
    """
    Modelo base que permite tener registro de quien y cuando se realizo la
    creacion del objeto, ademas de proveer una forma de eliminar segura, sin
    eliminar realmente el objeto sino cambiando su estado a inactivo.
    """
    fecha_registro = models.DateTimeField('Fecha de registro', 
        auto_now_add=True)
    usuario_registro = models.ForeignKey(settings.AUTH_USER_MODEL,
        verbose_name='Usuario que registra')
    activo = models.BooleanField(default=True)
    objects = BaseManager()

    def __str__(self):
        return '%s - %s' % (self.usuario_registro.username,
            self.fecha_registro)

    def eliminar(self):
        """ Elimina de forma segura, solo inactivando el objeto """
        self.activo = False
        super(Base, self).save()



class ArchivoAdjunto(Base):
    """ 
    Archivo de proposito general, los cuales son usados por cualquier modelo
    que herede de Base.
    """
    base = models.ForeignKey('comun.Base', related_name='modelo_adjuntable')
    archivo = models.FileField('Archivo adjunto', upload_to='adjuntos')

    class Meta:
        verbose_name_plural = 'Archivos adjuntos'
        permissions = (
            ('view_archivoadjunto', 'Puede ver archivos adjuntos'),
        )

    def __str__(self):
        return self.get_nombre_archivo()

    def get_nombre_archivo(self):
        """ Retorna el nombre del archivo sin la ruta en la que se ubica """
        return os.path.basename(self.archivo.name)


class Comentario(Base):
    """ 
    Comentario de proposito general, los cuales son usados por cualquier modelo
    que herede de Base.
    """
    base = models.ForeignKey('comun.Base', related_name='modelo_comentable')
    texto = models.TextField()

    class Meta:
        verbose_name_plural = 'Comentarios'
        permissions = (
            ('view_comentario', 'Puede ver los comentarios'),
        )