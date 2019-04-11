from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    
    def __str__(self):
        return 'Nombre {} tipo {}'.format(self.nombre, self.tipo)



class Factura (models.Model):
    cliente = models.CharField(max_length=100)
    numero = models.IntegerField(null= True)
  
    def __str__(self):
        return 'cliente {} '.format(self.cliente)


    


class Compra (models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="producto_id")
    cantidad = models.IntegerField()
    precio = models.IntegerField(null = True)
    nrofactura = models.ForeignKey(Factura, on_delete=models.CASCADE, null=True, related_name="compras")
    fecha = models.DateField(null=False, blank=True)
   

    def totalin (self):
        totalin=0
        totalin = self.precio * self.cantidad
        return (totalin)
    
    def __str__(self):
        return 'producto {} cantidad {} precio {} fecha '.format(self.producto, self.cantidad, self.precio, self.fecha)
