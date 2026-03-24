from enums.tipoproducto import TipoProducto

class Producto():
    
    def __init__(self, nombre: str, precio: float, cantidad: int, tipo: TipoProducto):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.tipo = tipo
        
    def vender_producto(self, dinero_ingresado) -> str:
        if dinero_ingresado >= self.precio:
            if self.cantidad > 0:
                self.cantidad -= 1
                return "True"
            else:
                return "No hay inventario suficiente."
        else:
            return "Dinero insuficiente."