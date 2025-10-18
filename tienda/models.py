from django.db import models
from django.utils.text import slugify
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    #crea slugs(titulo unico)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos/',null=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE, related_name='productos')
    
    def __str__(self):
        return self.nombre
    
    