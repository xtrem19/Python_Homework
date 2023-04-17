# Homework 4
# 5 exercises with conditionals: if, if else and elif

print('Example If')
a = 3
b = 0
if a > b:
    print('A es mayor que B, a > b')
# A es un número positivo

print('------------------------------------------')
#Example If - Else
print('Example If else')
if a < b:
    print('a < b = Si se cumple')
else:
    print('a < b = No se cumple')

print('------------------------------------------')
#Example If elif else
print('Example if elif else')

if a > b:
    print('a > b, A es un numero positivo')
elif a < b:
    print('a < b, A es un numero negativo')
else:
    print('A es cero')

print('------------------------------------------')
#Example nested conditions

c = 8%3
if c > 0:
    print('La division tiene residuo')
    if c > 1:
        print('El residuo es mayor a 1')
    else:
        print('El residuo es:', c)
elif c ==0:
    print('El residuo es 0')
else:
    print('Revisa la division')

print('------------------------------------------')
#Example nested conditions
print('Para solicitar una licencia de conducir')
edad = int(input('Digite la edad de la persona: '))
#Condicional elif
if edad<16:
    print('Todavía no puede conducir')
elif edad<18:
    print('Puede obtener un permiso para conducir')
elif edad<70:
    print('Puede obtener la licencia estandar')
else:
    print('Requiere de una licencia especial')