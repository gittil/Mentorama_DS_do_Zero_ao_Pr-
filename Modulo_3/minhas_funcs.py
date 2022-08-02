def identifica_pares_lista(lista):
    """\n
    Retorna lista de numeros pares na lista de input
    """
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            continue
    return pares

def soma(x,y):
    return x+y

def multiplica(x,y):
    return x * y

def encontra_max_lista(lista):
    return max(lista)

def identifica_pares(x):
    if x % 2 == 0:
        print(x,"é par")