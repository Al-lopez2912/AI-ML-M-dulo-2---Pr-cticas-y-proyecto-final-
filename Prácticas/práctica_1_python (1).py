# -*- coding: utf-8 -*-
"""Práctica #1 python.ipynb



#ejercicio 1

Nombre_del_producto = "Batida"
Precio_del_producto = 150
En_oferta = False
cantida_stock = 50

print(Nombre_del_producto)
print(Precio_del_producto)
print(En_oferta)
print(cantida_stock)
print(type(Nombre_del_producto), type(Precio_del_producto), type(En_oferta))

#Ejercicio2

precio = 18.75
pago = 20
vuelto = pago - precio

print(f"devuelta = {vuelto}")

#ejercicio3

monto = 39
billetes_de_diez = monto // 10
sobrante = monto % 10

print("Billetes de diez:", billetes_de_diez, "Sobrante:", sobrante)

#ejercicio4

numero1 = float(input("Dime el primer número"))
numero2 = float(input("Dime el segundo número"))

suma = numero1 + numero2
print(f"La suma de {numero1} y {numero2} es {suma}")

#ejercicio 5

nota = float(input("Cuál es tu nota?"))

if nota >= 90:
  letra = "A"
elif nota >= 80:
  letra = "B"
elif nota >= 70:
  letra = "C"
else:
  letra = "F"

print(f"Nota {nota}: {letra}")

#Ejercicio integrado 1-4

#Una tienda da descuento según el monto total de la compra: 15% si la compra es de $200 o más, 10% si es de $100 a $199, y sin descuento si es
#menos de $100. Pídele al usuario el monto de su compra con input(), calcula el descuento que le corresponde, y muestra con f-strings el monto
#original, el porcentaje de descuento aplicado, y el precio final después del descuento.
#Necesitas entrada de datos (Paso 3), variables y tipos (Paso 1), operadores para calcular el descuento (Paso 2), y condicionales para decidir qué porcentaje aplica
#(Paso 4). Todo en un solo programa.

monto = float(input("Cuál es el monto de su compra?"))

if monto >= 200:
   descuento = 0.15
elif monto >= 100:
   descuento = 0.10
else:
   descuento = 0

precio_final = monto - (monto * descuento)

print(f"Monto original: ${monto}")
print(f"Descuento aplicado: {float(descuento*100)}%")
print(f"Precio final: ${precio_final}")

#calculadora de propina inteligente

nombre = str(input("Hola, cúal es tu nombre: "))
monto = float(input(f"{nombre} ,por favor dime el monto de la cuenta:"))
cantidad_personas = int(input("cuantas personas vienen contigo?"))

propina_porcentaje = 0.0
if monto < 20:
  propina = 0.10
elif monto <= 50:
  propina = 0.15
else:
  propina = 0.20

if cantidad_personas > 4:
   propina += 0.05

propina = monto * propina
total = monto + propina
pago_por_persona = total / cantidad_personas

print(f"Monto de la propina:{propina}")
print(f"Total a pagar:{total}")
print(f"Pago por persona:{pago_por_persona}")
