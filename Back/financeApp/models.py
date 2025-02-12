from django.db import models

# Create your models here.

class Transaccion(models.Model):
    TYPE_CHOICES = [
        ('ingreso', 'Ingreso'),
        ('gasto', 'Gasto'),
    ]
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=TYPE_CHOICES)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo}: {self.descripcion} - {self.monto}"