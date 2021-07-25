from django.db import models

# Create your models here.

class Project(models.Model):
    #verbose_name renombrar los campos al español
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción")
    image= models.ImageField(verbose_name="Imagen", upload_to='projects')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")
    URLField = models.URLField(null=True, blank=True, verbose_name="Dirección web")

    class Meta:
        verbose_name='proyecto'
        verbose_name_plural='proyectos'
        ordering = ["-created"]

    #modificar el titulo en el administrador de Django
    def __str__(self):
        return self.title