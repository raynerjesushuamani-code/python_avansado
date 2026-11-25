# modularidad 
la ` modularidad` consiste en dividr un programa grande en archivos pequñeos y reutilizables llamdados `modulos`, cada modulo es simllemente un archivo `py`
**ventajas**
`reutilizacion`escribews el codigo una vez y lo mucho que usas en muchos programas 
`organizacon  ` cada archiivo tiene una responsabilidad clara
`mantenimiento` es mas dificil encontrat y corregir errore que  cometistes cuando esatbas con ella 
`trabajo en equipo ` cada persona puede desarrolar su propio modulo  
## 1. crear un modulo
basta con crear una rchivo con sal extencion `.py` ejemplo `matematicsaa s.py`
## 2. importar un mmodlulo
la manera de como reutilzamos lo modulos es haciendo uso de la palabra reservadad import` esto s edebe declasraf en el arvhico donde reutilizaremos ciertas funcines o variables  de un modulo .
para imprat un modulo completo usamos  `impor nombre archivo `
`matematicas .py`
```python
def suma(a,b):
    return a+b
def resta (a,b):
    return a-b
```
`main.py`
```python
import matematicas 
## para ahcer uso una de las funciones tengo que accder al archivo luego un punto y el nombre de dato funcion qure deseamoas utilizar 
matematicas.resta(5,8)
```
### 3. 
a veces es necsario importar solo una parte del modulo esto se usa c uaando deseamos utilizar partes especificas de un modulo para esto utilizamos `from_modulo import parte_especifica`
`mate.py`
```python
def resta(a,b):
    return a-b
def suma(a,b):
    return a+b
PI=3.1415
```

`main.py`
```python
from mate import PI
```
## PAQUETES (CARPETAS DE MODULOS)


