# funciones en python
las funciones nos permiten ordenar mejor el codigo y reutilizarlo cuando sea necesario
```python
# ejemplo deseamos crear un programa en python que nos permiten sumar dos numeros
numero_uno:int=45
numero_dos:int=70
numero_tres:int=78
numero_cuatro:int=20
suma:int=numero_uno+numero_dos
suma_dos:int=numero_tres+numero_cuatro
print(suma)
print(suma_dos)
```
como hacemos reutilizable el ejercicio anterior y mas lejible.
para eso utilizaremos funciones.
la carateristica de un funcion en python es la siguiente:
1. debe comenzar con la palabra reservda `def`.
2. debe tener un nombre que de a entender que realizara la funcion
3. debera tener parametros estos estaran encerrados en `()` no todas las funciones resistiran parametros aun asi debera tener los `()`
4. las funciones deberan retornar datos atraves de la palabra reservada `return`
```python
# crear un programa que me permita sumar dos numeros
def sumar(a,b):
    return a+b

print(sumar(78,56))
print(sumar(45,5))
```
## funciones avanzadas
existen tres grandes conceptos para poder entender el uso avanzado de las funciones
1. argumentos , parametros posicionales y nominales, *args y +kargs.
2. anotaciones en la salida de una funcion.
3. recursividad.

```python
# anotaciones en una funcion
def suma(a:int,b:float)->int:
    return a+b
# crear solo las anotaciones de una funcion que resiva cuatro numeros enteros y como salida que me muestre los 4 numeros enteros en una lista
def mostrar_numeros(a:int, b:int, c:int, d:int) -> list[int]:
    return[a,b,c,d]
```
**Argumentos parametros**
- **parametros** - los parametros son las variables que se declaran en la definicion de la funcion
- **argumentos** - es el dato concreto enviado en el llamado de la funcion
- **nota** en ambos casos tenemos los posicionales/nominales
```python
# parametros
def suma(a+b): # en este caso tenemos una funcion suma que recibe dos parametros a,b
suma(34,45) # en este caso estoy llamando a la funcion pasandole como argumento pasando los daatos
# en este caso en concreto podemos decir que estamos en frente a una funcion que tiene parametros posicionales eso significa qyue cada valor reemplazara en el orden que le pasemos a las variables,, 34 ->a , 45->b

def login(usuario="",password=""):
    return " acceso correcto"
login(password="12345678",usuario="tupapi")
# esta funcion es una funcion nominal porque para pasar los valores tengo que indicar la variable a la que se le va asociar el parametro de la funcion

## conociendo mas sobre funciones parametros y argumentos 
sobre los parametros argumentos nominales  es ampliamente usado para configuraciones para distinats configuraciones y que se puede pasar solo los argumentos  qeu se usaran y dejar los parametros por defecto si no se van amodificar
```python"
# tenemos un programa que me permite acceder a internet que tien paraemtros por defecto sin embargo sis e actualiza uno de los accesos se podra odificar  el valor 
## primer casxo acceso por defecto 
# def config(a:int,b:int|float,h):
def config (user="admin",pass"1234",port="8080",BSSID="wifi"):
    return "conectando a internet"
config(BBBID=laboratorio1)  
# segundo caso 1 bssid cambi por el del laboratorio1
def config (user="admin",pass"1234",port="8080",BSSID="wifi"):
    return "conectando a internet"
config(BBBID=laboratorio1) 

## reyner desea conectarse a l wifi de ana luz pregunta como se llama tu wifi y cual es la contraseña. respuesta le dice el wifi es a56 y su contraseña  es 12345678
def config (user="admin",pass"1234",port="8080",BSSID="wifi"):
    return "conectando a internet"
config(BBBID="A56",pass="12345678" ) 
```
### conociendo *args y **kargs (empaquetados y desempaquetados de argumentos posionales)
esta tecnica nos permite enpaquetar nuestros argumentos cuando no sabemos la cantidad de datos que vamos a pasar, imaginemos que nos piden una funcion pra sumar  n cantidada de numeros la solucion sereia empaquetar los argumentos y luego desempaquetamos para ello en la definicion e la funcion dentro de los parametros debemos uasr el,operador `*` delante del nombre del parametro posicional esto hara que todos los argumentos se almacenen en una tuplaa(lista) esto nos permite recorrer dentor de sus elementos para poder desempaquetarlo y realizar las operaciones necesarias 
```python
# deseasmo crearf una funcion que nos permita sumar n cantidadd de nunmeros 
# n es numero variable puede ser 3,5,7,8,9
def suma(*args):
    #*args = (2,5,7,9,)
    acumulado=0
    for i in args:
        acumulado+= i
    return acumulado
    print(suma(2,5,7,9))    

```
### desempaquetando argumemetnos nominales  
en ese caso como en el anterior utilizaremos el,operador * la causitica es el mismo sin embargo para desempaquetar argumentos nominales uaasaremos **  delante  del nombre de parametro nominal diferencia  del anterior esto se empaqeuta en un diciconario 

```python
# debemos crear una funcion que me permita saber encontrara la persona conj amyor calificacion 
def mejor_alumno (**kwargs):
    # **kwarsg={clave:valor}
    # ejor_aluno(noemi=20,eduardo=18,david=19)
    nota_maxima
    for alumno,note in kwarsg.items():
        if nota > nota maxima:
            nota_maxima = nota 
            mejor_alumno = alumno
    return mejor_alumno
mejor_aluno(noemi=20,eduardo=18,david=19)        
```