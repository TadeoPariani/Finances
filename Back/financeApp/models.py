from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Cuenta(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    alias = models.CharField(max_length=100, null=True)
    cvu = models.CharField(max_length=100, null=True) 
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, null=True)
    userID = models.ForeignKey(
        User,  
        on_delete=models.CASCADE, 
        null=True
    )

    def __str__(self):
        return self.nombre
    
class Presupuesto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    monto_maximo = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    mes = models.DateField()
    cuentaID = models.ForeignKey(Cuenta, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Presupuesto {self.categoria} - {self.monto_maximo}"

class Transaccion(models.Model):
    TYPE_CHOICES = [
        ('ingreso', 'Ingreso'),
        ('gasto', 'Gasto'),
    ]
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=TYPE_CHOICES)
    fecha = models.DateField()
    categoriaID = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    cuentaID = models.ForeignKey(Cuenta, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.tipo}: {self.descripcion} - {self.monto}"
