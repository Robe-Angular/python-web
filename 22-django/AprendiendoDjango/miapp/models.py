from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default='null',verbose_name="Imagen", upload_to='articles')
    public = models.BooleanField(verbose_name="Público")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creado') #Cuando se crea el registro
    updated_at = models.DateTimeField(auto_now=True, verbose_name='editado') #Cuando se actualiza

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ['id']

    def __str__(self):
        if self.public:
            publico="Público"
        else:
            publico="privado"

        return f"{self.title} creado el {self.created_at} ({publico})"


class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField()
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        