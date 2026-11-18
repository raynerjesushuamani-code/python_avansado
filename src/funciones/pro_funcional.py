# para map()
## recuerde map sirve para  transformar todos los elementos
## ejercico1: tienes una lista de hnmeros y quieres obtener una nueva lista con el cubo (elevado al 3) de cada numero.
numeros:list[int]=[1,2,3,4,]
nueva_lista=list(map(lambda e: e**3,numeros))
print(nueva_lista)

# ejercicio para filter()
## ejercicio 2. tienes una lsita d etemperaturas (algunas bajo cdreo).filtra la lsita paar quedarte solo con las temperaturasd positivas (mayores a 0 )
temp:list[int|float]=[-2,10,0,-18,-23.0,3,9,]
nueva_temp=list (filter(lambda t:t>0,temp))
print(f"las temperaturas mayores a 0 son: {nueva_temp}")
# ejercicio combinado map()y filter()
## tienes una lista de numeros primero flitra para quedarte solo con los numeros pares luego usa map para multiplicarlos *10 los numeros pares
num:list[int]=[1,2,3,4,5,6,7,8,9]
# nuevo_par=list(filter(lambda x:x % 2==0,num))
#nuevo_par:list[int]=filter(lambda x:x % 2==0,num)
#print(f"numeros pares son : {nuevo_par}")
# multi=list(map(lambda x: x*10,nuevo_par))
multi=list(map(lambda x:x*10,(lambda x:x % 2==0,num)))
print(f"las multiplicaones + 10 {multi}")











