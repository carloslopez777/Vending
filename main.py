from entidades.producto import Producto
from enums.tipoproducto import TipoProducto

print("Ingresa el nombre del producto:")
nombre = input("")

print("Ingresa el precio del producto:")
precio = float(input(""))

print("Ingresa la cantidad de productos:")
cantidad = int(input(""))

print("Ingresa el tipo de producto:")
tipo = input("")

print("Tipo de Producto")
for producto in Producto:
    print(f"{producto.value} - {producto.name}")
print("Ingresa el tipo del producto:")
opcion = int(input(""))

producto1 = Producto(nombre, precio, cantidad, TipoProducto(opcion))