
def countdown(start):
    cuenta_atras = []
    for i in range(start, -1, -1):
        cuenta_atras.append(i)          # Cuenta regresiva
    return cuenta_atras
lista = countdown(5)
print(lista) 

def imprimirdevolver(lista):
    print(lista[0])
    return(lista[1])                    # Imprimir y devolver
lista = [1,2]
devolver = imprimirdevolver(lista)
print(devolver)

def sumaprimerolista(lista):
    return(lista[0] + len(lista))

lista = [1,2,3,4,5]                     # Primero más longitud
devolver = sumaprimerolista(lista)
print(devolver)

def mayores_que_el_segundo(lista):
    lista_nueva = []
    segundo_valor = lista[1]
    i = 0
    for i in lista:
        if i > segundo_valor:
            lista_nueva.append(i)         # Valores mayores que el segundo
    return lista_nueva
    if len(lista_nueva) < 2:
        return("false")
lista = [5,2,3,2,1,4]
devolver = mayores_que_el_segundo(lista)
print(devolver)


def lenght_and_value(b,c):
    
    lista_nueva = [c] * b
    return lista_nueva                  # Esta longitud, ese valor

resultado1 = lenght_and_value(4, 7)
resultado2 = lenght_and_value(6, 2)
print(resultado1)
print(resultado2)

