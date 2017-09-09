# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-06 02:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArchivoAdjunto',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='comun.Base')),
                ('archivo', models.FileField(upload_to='adjuntos', verbose_name='Archivo adjunto')),
            ],
            options={
                'permissions': (('view_archivoadjunto', 'Puede ver archivos adjuntos'),),
                'verbose_name_plural': 'Archivos adjuntos',
            },
            bases=('comun.base',),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='comun.Base')),
                ('texto', models.TextField()),
            ],
            options={
                'permissions': (('view_comentario', 'Puede ver los comentarios'),),
                'verbose_name_plural': 'Comentarios',
            },
            bases=('comun.base',),
        ),
        migrations.AddField(
            model_name='base',
            name='usuario_registro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario que registra'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelo_comentable', to='comun.Base'),
        ),
        migrations.AddField(
            model_name='archivoadjunto',
            name='base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelo_adjuntable', to='comun.Base'),
        ),
    ]
