stock = 50

print("***** Cine Estrella *****")
print("Bienvenido al sistema de venta de entradas del Cine Estrella")
print("1. Ver entradas disponibles")
print("2. Comprar entradas")
print("3. Devolver entradas")
print("4. Salir")

opcion = input("Selecciona una opción (1-4): ")

if opcion == '1':
    print(f"Entradas disponibles: {stock}")

elif opcion == '2':
    cantidad = input("¿Cuántas entradas desea comprar?: ")
    if not cantidad.isdigit():
        print("Debe ingresar un número entero válido.")
    else:
        cantidad = int(cantidad)
        if cantidad > stock:
            print("No hay suficientes entradas disponibles.")
        elif cantidad <= 0:
            print("Debe ingresar un número mayor a cero.")
        else:
            stock -= cantidad
            print(f"Compra exitosa. Quedan {stock} entradas.")

elif opcion == '3':
    cantidad = input("¿Cuántas entradas desea devolver?: ")
    if not cantidad.isdigit():
        print("Debe ingresar un número entero válido.")
    else:
        cantidad = int(cantidad)
        if cantidad <= 0:
            print("Debe ingresar un número mayor a cero.")
        else:
            stock += cantidad
            print(f"Se han devuelto {cantidad} entradas. Total disponible: {stock}")

elif opcion == '4':
    print("Gracias por usar el sistema de ventas del Cine Estrella. ¡Hasta pronto!")

else:
    print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")