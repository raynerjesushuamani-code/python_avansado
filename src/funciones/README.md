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

<<<<<<< HEAD
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
=======
```



## funciones anonimas
las funciones anonimas en python son llamadas `lamba`,estas funciones tiene las siguientes propiedades:
1. se escribe en una unica sentencia`(linea)`
2. no tiene nombre`(anonima)`
3. su cuerpo conlleva un `return` implicito.
4. puede recibir cualquier numero de parametros.

la estructura para definir una funcion landa `lambda` es la siguiente:
1. escribir la palabra reservada `lambda` 
2. especificar la cantidad de parametros.
3. indicar los datos de retorno
```python
lambda a,b: a+b
```
> [!TIP] puesto que esta funcion es anonima para ejecutarla debemos almacenar la funcion en una variable
 ```python
suma=lambda a,b: a+b
suma(3,6)
```
## Documemntacion
python nos permite documentar una funcion con el objetivo de explicar mejor determinadas zonas de nuestro codigo, para esto uzamos una cadena de texto despues de la difinicion de una funcion, a esta cadena de texrto se le conoce como `docstring` y esta delimitado por triples comillas `"""aqui el texto"""`
```python
def suma(a,b):
    """
    funcion para realizar la suma de dos numeros
    """
# los docstring tambien nos permite explixcvar los parametros que recibe los datos de salida
def resta(a,b):
    """
    a= un numero entero.
    b= un numero entero.
    en ambos casos a,b deben recibir valores menores 0.
    retronara un dato entero <int> positivo
    """
    return a-b
```
> [!WARNING] en el proceso de documentacion tener en cuenta de incluir a lop menos lo siguiente: 
>1. breve explicacion sobre que hace la funcion  
>2. especificaciones y caracteristicas de los parametros incluyendo sus tipos . 
>3. restricciones de la funcion.  
>4. el valor que retorna y sus caracteristicas

## type-hints (anotaciones de tipo)
nos permite indicar que tipo de datos recibiran una variable, parametro y el valor de retorno de una funcion.
para utilizarlos debemos indicar el tipo de dato despues del separador`:`, en el caso del valor de retorno usaremos `->` luego el tipo de dato y finalmente el separador`:` que indica el inicio del bloque de codigo de la funcion.
las `anotacines tipo` son una herramienta que nos perite complementar la documentacion de nuestro codigo
**tenemos los siguientes**
- **simple**
- int -> numeros enteros
- float -> decimales
- bool -> datos boleanos (verdad o falso)
- str -> datos de tipo texto o cadena
- list -> listas `[]`
- tuple -> tuplas `()`
- dict -> diccionarios `{}`
-**compouestos**
existen casos en os que necesitamos mas exprecividad en la *anotacion de tipos*  ¿que ocurre si queremos indicar una *lista de cadenas* o un *conjunto de enteros*.?
- list[str] -> lista de cadenas de texto
- list[int] -> lista de numeros enteros
-dict[str,float] -> diccionario domnde las claves son cadenas de texto y los valores son flotantes/decimales
-**multiples**
 en el caso que queramoa indicar que un determinado parmetro puede ser de un `tipo o de otro` tenemos que espicificarlo usando el operador `|`
 - tuple|dict -> puede ser datos de tipo tupla o diccionario
 - list[srt|int] -> lista cuuyos elementos pueden ser cadenas de texto o enteros
 - dict[srt|int,float|int] -> diccioanrio
<<<<<<< HEAD

=======
## closure
una `closure` o `clausura` son funciones que establececn una funcion interioi, o retornan una funcion estas funciones se caracterizan por recrear el valor de los argumentos que se le pasa.
```python
def multiplicando(n):
    def multiplicador(m):
        return n*m
    return multiplicador
```

## Programacion funcional

Python es un lenguaje de programación multiparadigma, y uno de sus paradigmas que mejor funcionan es la `funcional`.

Python usa tres `map()`, `filter()`, `reduce()`, pero nosotros solo usaremos `map()` y `filter()`.

Estas funciones integradas de python sirven para procesar y transformar colecciones de datos(listas,diccionarios) de manera muy eficiente:

> [!tip] Importante:
> Las funciones `map()` y `filter()` reciben dos parámetros primero la funcion a ejecutar y segundo el iterable en que va actuar. La funcion que recibe como parametro puede ser normal (`def`) o puede ser anonima(`lambda`).

### 1. map()

map aplica una funcion especifica a cada una de los elementos de una coleccion (iterable) y devuelve un nuevo iterable con los resultados.

```python
## De una lista de numeros deseamos calcular la potencia 2 de cada numero
numeros:list[int]=[2,4,6,8,7]

## Cuando deseamos trabajar con una funcion anonima tenemos que declarar primero la funcion antes de pasarla por parametro.
def f(x):
    return x**2

## Una vez creada pasamos la funcion como parametro
map(f,numeros)

## Cuando deseamos trabajar con funciones anonimas usamos lambda dentro del parametro.
map(lambda x:x**2,numeros)
```

### 2. Filter()

Filter para cada elemento de una coleccion por una funcion y soli se queda con aquellos elementos donde la funcion devuelve True (es decir, filtra los datos segun su condicion).

```python
# Imagina

filter(lambda n:n % 2==0,numeros)
```

> [!WARNING] Nota importante
> Tanto `map()` como `filter()` no devuelve lista directamente, sino iteradores. Esto es para ahorrar memoria (evaluacion perezosa o lazy evaluation). Si quieres ver el resultado como una lista tradicional, siempre debes envolver en `list()`.
# de una lsita de numeros enteros  deseamos calcular la potencia 2 de cadadd numero 
```python
numeros:list[int] ¨[2,4,7,8,6]
## cuando deseamos trabajar con una funcion anonima tenemsos que declarar primero la funcion nates de pasarla por parametro
def (x):
    return  x**2
## cuando deseam os trabajar con funciones anonimas usa,mos lambda  dentro ndel parametro
map(lambda x:x**2,numero)
```
