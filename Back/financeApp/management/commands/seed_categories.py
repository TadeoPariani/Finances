from django.core.management.base import BaseCommand
from financeApp.models import Categoria

class Command(BaseCommand):
    help = 'Popula la base de datos con categorías predeterminadas'

    def handle(self, *args, **kwargs):
        categorias = ["Alimentación", "Transporte", "Salud", "Entretenimiento", "Educación", "Cuentas", "Servicios", "Varios"]
        
        for nombre in categorias:
            Categoria.objects.get_or_create(nombre=nombre)
        
        self.stdout.write(self.style.SUCCESS('Categorías creadas exitosamente.'))
