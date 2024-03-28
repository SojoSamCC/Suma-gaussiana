guion="-"
num_de_flechas=100
print()
print("¡Te doy la bienvenida a este programita para hacer la suma de todos los números desde el 1")
print("hasta el número que me digas! (Mejor conocido como suma gaussiana).")
print()
print("Mucho ojo con ingresar correctamente todos los datos que te va ir pidiendo el programa.")
print()
print("Si deseas apoyarme te dejo mi alias de Mercado Pago Argentina: sojo.sam.mp")
print()
print("También te dejo mi ig por si deseas seguirme: @therealdusa")
print()
print("Bueeeno, ahora sí. Comencemoooos.")
print()
for _ in range(num_de_flechas):
      print(guion, end="")
print()
print()
def numeradorf():
        valor_de_suma_hasta=int(input("Ingrese valor del número para realizar la suma de todos los enteros hasta él: "))
        n=valor_de_suma_hasta
        n_mas_1=valor_de_suma_hasta+1
        numerador=n*(n_mas_1)
        return numerador

def suma_de_numeros_hasta():
        valor_de_suma_total=(numeradorf())/2
        return valor_de_suma_total

def repetir_suma():
        valor_de_suma_total=suma_de_numeros_hasta()
        return print(f"El valor de la suma hasta el número que ingresaste es: {valor_de_suma_total}")   

repetir_suma()

while True:        
    continuar=input("¿Desea realizar otra suma? (Y/n): ")
    if continuar!="n":
        repetir_suma()
    else:
        print()
        break

for _ in range(num_de_flechas):
      print(guion, end="")
print()
print()
print(" ¡Muchas gracias por utilizar este script!")
print()
print(" Que tengas un lindo día.")
print()
print("-SojoSam.")
print()
print
input("--Presiona cualquier tecla para cerrar el programa--")
exit()