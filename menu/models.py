from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    orden = models.PositiveIntegerField( default=0)

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        if not self.id:  # Si es una nueva instancia
            # Obtener el último valor de orden y sumarle 1
            ultimo_orden = Categoria.objects.order_by('-orden').first()
            if ultimo_orden:
                self.orden = ultimo_orden.orden + 1
            else:
                self.orden = 1
        super().save(*args, **kwargs)
class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre