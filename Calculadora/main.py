# EL OBJETIVO ES HACER UNA CALCULADORA TOTALMENTE FUNCIONAL 
# APLICANDO TODO LO QUE APRENDA EN EL CURSO
# VERSION 1 - USANDO IF, SIN CONTROL DE ERRORES Y NO REDUNDANTE

print("************ CALCULADORA ************")
print("******* BY MIGUELANGEL TORRES *******")

# ENTRADA DE DATOS - NUMEROS CON LOS QUE SE VA A TRABAJAR
# TODO LO INGRESADO EN UN INPUT ES DE FORMATO STRING - MANTENER PRESENTE

numero1 = int(input("\nIngrese el 1er numero - DEBE SER ENTERO \n"))
numero2 = int(input("Ingrese el 2do numero - DEBE SER ENTERO \n"))

# ELECCION DE OPERACIONES
print(f"\nLos numeros ingresados son {numero1} y {numero2}\nQue desea hacer con ellos?\n")
print("Opcion 1 - SUMA")
print("Opcion 2 - RESTA")
print("Opcion 3 - MULTIPLICACION")
print("Opcion 4 - DIVISION")

opcion = int(input("Indique la opcion: "))
print("-------------------------------------")

# CONDICIONALES - OPERACIONES
if opcion == 1:
    numero3 = numero1 + numero2
    print(f"El resultado de la SUMA es {numero3}")
elif opcion == 2:
    numero3 = numero1 - numero2
    print(f"El resultado de la RESTA es {numero3}")
elif opcion == 3:
    numero3 = numero1 * numero2
    print(f"El resultado de la MULTIPLICACION es {numero3}")
elif opcion == 4:
    numero3 = numero1 / numero2
    print(f"El resultado de la DIVISION es {numero3}")
else:
    print("La Opcion ingresada esta fuera de rango.")    


# PARA DESPUES
# NUMERO DE OPERACIONES
# conteo_operaciones = 0