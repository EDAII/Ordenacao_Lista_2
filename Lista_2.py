import numpy as np
import sys
import ipdb
import time
from math import sqrt


# Gera valores inteiros aleatorios de 1 ate 100000
def gera_valor_aleatorio():
    valor = np.random.randint(0, 100000)
    return valor


# Gera o vetor de valores randomicos
def gera_lista():
    lista = []
    for i in range(limite_superior):
        numero = gera_valor_aleatorio()
        lista.append(numero)
    return lista


# Algoritmo de ordenacao insertion sort, iniciado a partir do segundo elemento
def insertion_sort(Lista):

    for j in range(1, len(Lista)):

        pivot = Lista[j]
        i = j-1

        while (i > -1) and pivot < Lista[i]:
            Lista[i+1] = Lista[i]
            i = i-1
        Lista[i+1] = pivot

    return Lista


# Gera um vetor de indice correspondente ao tamanho da lista de elementos
def gera_indice(quantidade_numeros, gap_percentage):
    vetor_de_indice = [i*gap_percentage for i in range(quantidade_numeros//gap_percentage)]
    vetor_de_indice.append(quantidade_numeros-1)

    return vetor_de_indice


# Busca binaria em uma lista de elementos
def busca_binaria(lista, valor):
    posicao = -1
    if lista:
        l = 0
        r = len(lista)-1
        mid = (l+r)//2
        if(l < r):
            if(lista[mid] == valor):
                posicao = mid
            elif (lista[mid] < valor):
                posicao = mid + 1 + busca_binaria(lista[mid+1:], valor)
            else:
                posicao = l + busca_binaria(lista[:mid], valor)
        elif lista[0] == valor:
            posicao = 0
    return posicao


# Busca sequencial no indice da lista
def busca_no_indice(indice, lista, valor):
    indice_fim = len(indice)-1
    posicao = -1

    if indice and lista:
        if lista[indice[0]] <= valor and lista[indice[indice_fim]] > valor:
            for i in range(indice_fim+1):
                if lista[indice[i]] > valor:
                    intervalo = [indice[i-1], indice[i]]
                    break;
            posicao_relativa = busca_binaria(lista[intervalo[0]:intervalo[1]], valor)
            if not(posicao_relativa == -1):
                posicao = intervalo[0] + posicao_relativa
        elif lista[indice[indice_fim]] == valor:
            posicao = indice[indice_fim]

    return posicao


# Busca um elemento na lista de elementos
def main(quantidade_numeros, gap_percentage):
    n = input('Digite o valor que deseja procurar no vetor: \n')
    lista_de_valores = gera_lista(limite_inferior, limite_superior, quantidade_numeros)
    vetor_de_indice = gera_indice(quantidade_numeros, gap_percentage)
    start = time.time()
    value = int(n)
    posicao = busca_no_indice(vetor_de_indice, lista_de_valores, value)
    if posicao >= 0:
        pass
        print "O valor esta localizado na posicao: ", posicao
    else:
        pass
        print "valor nao encontrado"
    # from guppy import hpy; h=hpy()
    # h.heap()
    end = time.time()
    print(end - start)


# Executa uma busca para cada elemento na lista_de_valores
def performance(quantidade_numeros, gap_percentage):
    lista_de_valores = gera_lista(limite_inferior, limite_superior, quantidade_numeros)
    vetor_de_indice = gera_indice(quantidade_numeros, gap_percentage)
    start = time.time()
    for n in lista_de_valores:
        value = int(n)
        posicao = busca_no_indice(vetor_de_indice, lista_de_valores, value)
        if posicao >= 0:
            pass
        else:
            pass

    end = time.time()
    print("Tempo de resposta: ", end - start)

if __name__ == '__main__':

    n = int(input('0 - Performance Automatica\n1 - Busca Manual: \n'))
    quantidade_numeros = 100000000
    print ("quantidade de elementos", quantidade_numeros)
    gap_percentage = int(sqrt(quantidade_numeros))
    # parametros do algoritmo
    limite_inferior = 0
    limite_superior = quantidade_numeros*10

    if n:
        main(quantidade_numeros, gap_percentage)
    else:
        performance(quantidade_numeros, gap_percentage)
