import random

colores_en_orden = 'rojo verde azul'.split()

def mezclar_colores(fichas,orden=colores_en_orden):
    'devuelve los items clasificados según el orden establecido'
    reverse_index = dict((x,i) for i,x in enumerate(orden))
    return sorted(fichas,key=lambda x: reverse_index[x])

def test_mezclar_colores(fichas,orden=colores_en_orden):
    'Devuelve True si cada color está en el orden correcto'
    reverse_index = dict((x,i) for i,x in enumerate(orden))
    orden_fichas = [reverse_index[ficha] for ficha in fichas]
    return all(x <= y for x,y in zip(orden_fichas,
                                     orden_fichas[1:]))

def random_fichas (n):
    'Se escoge de 1 a n (siendo n elección del usuario) el número de fichas de cada color de manera aleatoria'
    fichas = sum ([[color] * random.randint(1,n) for color in colores_en_orden],[])
    random.shuffle(fichas) # se mezclan las fichas
    return fichas

def main():

    while True:
        n = int(input("Ingrese el número de fichas: "))
        fichas = random_fichas(n)
        if not test_mezclar_colores(fichas):
            print('Error')
            print(fichas)
            break 
    print("Orden sin clasificar:",fichas)
    sorted_fichas = mezclar_colores(fichas) # se clasifican las fichas
    print("Orden clasificado:",sorted_fichas)
    assert test_mezclar_colores(sorted_fichas)

if __name__ == '__main__':
    main()