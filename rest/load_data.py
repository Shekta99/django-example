from .models import Tarea

tarea1 = Tarea(nombre="Hacer la compra", completada=False)
tarea2 = Tarea(nombre="Llevar el coche al taller",  completada=True)

tarea1.save()
tarea2.save()