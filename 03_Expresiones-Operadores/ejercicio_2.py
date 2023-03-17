## Expresiones.
'''
Las expresiones son combinaciones de constantes, variables, símbolos de operación, paréntesis y nombres de funciones especiales.

Una expresión consta de operandos y operadores. Según sea el tipo de objetos que manipulan, las expresiones se clasifican en: 

* aritméticas 
* relacionales
* lógicas
* carácter

El resultado de la expresión aritmética es de tipo numérico; el resultado de la expresión relacional y de una expresión lógica es de tipo lógico; el resultado de una expresión carácter es de tipo carácter.

Las expresiones aritméticas son análogas a las fórmulas matemáticas. Las variables y constantes son numéricas (real o entera) y las operaciones son las aritméticas.

* `+` - Este es el operador de suma y realiza la función de adicionar un operando al otro. 
* `-` - Este es el operador de resta y realiza la función de sustraer un operando de otro.
* `*` - Este es el operador de multiplicación y realiza la función de aumentar un operando en función de otro operando.
* `/` - Este es el operador de división y realiza la función de seccionar un operando en función de otro operando.
* `%` - Este es el operador de módulo y realiza la función de regresar el residuo de una división.
* `**` - Este es el operador de exponencial y permite obtener la potencia de un operando en función de otro operando.

A continuación se presentan algunos ejemplos de los operadores en código Python.
'''
# Operador +.
print('Operador +')
# python
a = 7 + 3
print('Resultado de a = 7 + 3 =',a,'y su clase es:', type(a))   #10 <class 'int'>
a = 5
b = 3
c = a + b
print('Si a = 5, b = 3 entonces c = a + b =',c, 'y su clase es:', type(c))  #8 <class 'int'>
print('Si 3+4 =', 3+4, 'y su clase es:', type(3+4)) #7 <class 'int'>

# Operador -.
print('Operador -')
# python
a = 6 - 2
print('Resultado de a = 6 - 2 =',a,'y su clase es:', type(a))   #4 <class 'int'>
a = 5
b = 3
c = a - b
print('Si a = 5, b = 3 entonces c = a - b =',c, 'y su clase es:', type(c))  #2 <class 'int'>
print('Si 2-6 =', 2-6, 'y su clase es:', type(2-6)) #-4 <class 'int'>

# Operador *.
print('Operador *')
# python
a = 3 * 4
print('Resultado de a = 3 * 4 =',a,'y su clase es:', type(a)) #12 <class 'int'>
a = 6
b = 3
c = a * b
print('Si a = 6, b = 3 entonces c = a * b =',c, 'y su clase es:', type(c)) #18 <class 'int'>
print('Si 5*7 =', 5*7, 'y su clase es:', type(5*7)) #35 <class 'int'>

# Operador /.
print('Operador /')
# python
a = 6 / 2
print('Resultado de a = 6 / 2 =',a,'y su clase es:', type(a)) #3 <class 'float'>
a = 5
b = 3
c = a / b
print('Si a = 5, b = 3 entonces c = a / b =',c, 'y su clase es:', type(c)) #1.6667 <class 'float'>
print('Si 10/3 =', 10/3, 'y su clase es:', type(10/3)) #3.3333 <class 'float'>

# Operador %.
print('Operador %')
# python
a = 8 % 4
print('Resultado de a = 8%4 =',a,'y su clase es:', type(a)) #0 <class 'int'>
a = 9
b = 2
c = a % b
print('Si a = 9, b = 2 entonces c =a%b=',c, 'y su clase es:', type(c)) #1 <class 'int'>
print('Si 10%3 =', 10%3, 'y su clase es:', type(10%3)) #1 <class 'int'>

# Operador **.
print('Operador **')
# python
a = 3 ** 3
print('Resultado de a = 3 ** 3 =',a,'y su clase es:', type(a)) #27 <class 'int'>
a = 2
b = 4
c = a ** b
print('Si a = 2, b = 4 entonces c =a ** b=',c, 'y su clase es:', type(c)) #16 <class 'int'>
print('Si 4**3 =', 4**3, 'y su clase es:', type(4**3)) #64 <class 'int'>

'''
Expresiones relacionales

* `<` - Este es el operador de menor que, y se utiliza en las expresiones relacionales para saber si un operando es menor a otro operando.
* `>` - Este es el operador de mayor que, y se utiliza en las expresiones relacionales para saber si un operando es mayor a otro operando.
* `==` - Este es el operador de igual que, y se utiliza en las expresiones relacionales para saber si un operando es igual a otro operando.
* `!=` - Este es el operador desigual que, y se utiliza en las expresiones relacionales para saber si un operando es diferente a otro operando.
* `<=` - Este es el operador de menor igual que, y se utiliza en las expresiones relacionales para saber si un operando es menor o igual a otro operando.
* `>=` Este es el operador de mayor igual que, y se utiliza en las expresiones relacionales para saber si un operando es mayor igual a otro operando.

NOTA: Como resultado de la aplicación de las expresiones relacionales, se obtendrá como resultado una salida booleana, es decir `TRUE` o `FALSE`.

A continuación se presentan algunos ejemplos de las expresiones relacionales en código Python.
'''
# Operador <.
print('Operador <')
# python
a = 3 < 3
print('Resultado de a = 3 < 3 =',a,'y su clase es:', type(a)) #False <class 'bool'>
a = 2
b = 4
c = a < b
print('Si a = 2, b = 4 entonces c = a < b =',c, 'y su clase es:', type(c)) #True <class 'bool'>
print('Si 4<3 =', 4<3, 'y su clase es:', type(4<3)) #False <class 'bool'>

# Operador >.
print('Operador >')
# python
a = 4 > 2
print('Resultado de a = 4 > 2 =',a,'y su clase es:', type(a)) #True <class 'bool'>
a = 5
b = 7
c = a > b
print('Si a = 5, b = 7 entonces c = a < b =',c, 'y su clase es:', type(c)) #False <class 'bool'>
print('Si 9>2 =', 9>2, 'y su clase es:', type(9>2)) #True <class 'bool'>

# Operador ==.
print('Operador ==')
# python
a = 5 == 5
print('Resultado de a = 5 == 5 =',a,'y su clase es:', type(a)) #True <class 'bool'>
a = 6
b = 9
c = a == b
print('Si a = 6, b = 9 entonces c = a == b =',c, 'y su clase es:', type(c)) #False <class 'bool'>
print('Si 6==2 =', 6==2, 'y su clase es:', type(6==2)) #False <class 'bool'>

# Operador !=.
print('Operador !=')
# python
a = 4 != 2
print('Resultado de a = 4 != 2 =',a,'y su clase es:', type(a)) #True <class 'bool'>
a = 5
b = 3
c = a != b
print('Si a = 5, b = 3 entonces c = a != b =',c, 'y su clase es:', type(c)) #True <class 'bool'>
print('Si 8!=8 =', 8!=8, 'y su clase es:', type(8!=8)) #False <class 'bool'>

# Operador <=.
print('Operador <=')
# python
a = 5 <= 3
print('Resultado de a = 5 <= 3 =',a,'y su clase es:', type(a)) #False <class 'bool'>
x = 7
y = 5
z = x <= y
print('Si x = 7, y = 5 entonces z = x <= y =',z, 'y su clase es:', type(z)) #False <class 'bool'>
print('Si 9<=4 =', 9<=4, 'y su clase es:', type(9<=4)) #False <class 'bool'>

# Operador >=.
print('Operador >=')
# python
a = 2 >= 8
print('Resultado de a = 2 >= 8 =',a,'y su clase es:', type(a)) #False <class 'bool'>
a = 3
b = 4
c = a >= b
print('Si a = 3, b = 4 entonces c = a >= b =',c, 'y su clase es:', type(c)) #False <class 'bool'>
print('Si 7>=3 =', 7>=3, 'y su clase es:', type(7>=3)) #True <class 'bool'>

'''
## Expresiones lógicas.


* `not` - Este es el operador lógico para realizar una negación, si el operando no se encuentra en el otro operando, la expresión se cumple y resulta en True, caso contrario, si la expresión no se cumple el resultado es False.
* `and` - Este es el operador lógico para realizar una conjugación, si cualquiera de los operandos presentes no se cumple en la expresión lógica, esta resulta en False, caso contrario, si toda la expresión lógica de conjugación se cumple el resultado es True.
* `or` - Este es el operador lógico para realizar una conjugación, si cualquiera de los operandos presentes no se cumple en la expresión lógica, esta resulta en False, caso contrario, si toda la expresión lógica de conjugación se cumple el resultado es True.
'''
# Operador and.
print('Operador and')
# python
print('4-1==3 and 5>6 es:', 4-1==3 and 5>6, ' y ', type(4-1==3 and 5>6)) #False <class 'bool'>
print('6+7 > 11 and 3==3 es:', 6+7 > 11 and 3==3, ' y ', type(6+7 > 11 and 3==3)) #True <class 'bool'>

# Operador or.
print('Operador or')
# python
print('4-1==3 or 5>6 es:', 4-1==3 or 5>6, ' y ', type(4-1==3 or 5>6)) #True <class 'bool'>
print('6+7 > 11 or 3==3 es:', 6+7 > 11 or 3==3, ' y ', type(6+7 > 11 or 3==3)) #True <class 'bool'>

# Operador not.
print('Operador not')
# python
print('not 5>6 es:', not 5>6, ' y ', type(not 5>6)) #True <class 'bool'>
print('not 5>4 es:', not 5>4, ' y ', type(not 5>4)) #False <class 'bool'>


'''
## Expresiones de carácter

A diferencia de las demás expresiones no existe un operador estático sino una búsqueda de secuencias, números o caracteres dentro de una variable.

Estas expresiones de búsqueda comúnmente llamadas expresiones regulares, sirven para captar ciertos elementos o patrones dentro de un valor.

Ejemplo:
'''
#
# python
print('Ejercicio Expresiones de caracter')
import re
frase = "Tengo 2 hijos que tienen 15 y 11 años"
patron = '[0-9]+' #Esta es una expresión regular
re.findall(patron, frase)
print(frase, '---> Buscar el patron:', patron)
print('Resultado:', re.findall(patron, frase)) #['2', '15', '11']

#
