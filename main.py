from entidades.producto import Producto
from enums.tipoproducto import TipoProducto
from colorama import Fore,init

print("Ingresa el nombre del producto:")
nombre = input("")

print("Ingresa el precio del producto:")
precio = float(input(""))

print("Ingresa la cantidad de productos:")
cantidad = int(input(""))

print("Tipo de Producto")
for tipo in TipoProducto:
    print(f"{tipo.value} - {tipo.name}")
print("Ingresa el tipo del producto:")
opcion = int(input(""))

print("Ingresa el dinero:")
dinero_ingresado = float(input())

producto1 = Producto(nombre, precio, cantidad, TipoProducto(opcion))

total_producto = producto1.vender_producto(dinero_ingresado)

if total_producto == "True":
    print(Fore.GREEN + "El producto se vendio correctamente")
    

else:
    print(Fore.RED + total_producto)
    