import numpy as np
import time


# Gera valores inteiros aleatorios de 1 ate 100000
def gera_valor_aleatorio():
    valor = np.random.randint(0, 100000)
    return valor


# Gera o vetor de valores randomicos
def gera_lista(limite_superior):
    lista = []
    for i in range(limite_superior):
        numero = gera_valor_aleatorio()
        lista.append(numero)
    return lista


# Algoritmo de ordenacao insertion sort, iniciado a partir do segundo elemento
def insertion_sort(Lista):
    for j in range(1, len(Lista)):
        chave = Lista[j]
        i = j-1
        while (i > -1) and chave < Lista[i]:
            Lista[i+1] = Lista[i]
            i = i-1
        Lista[i+1] = chave
    return Lista


# Recebe o limite superior do vetor de valores aleatorios e realiza a ordenacao
def main():
    tamanho = input('Digite o tamanho do vetor a ser gerado: \n')
    vetor = []
    vetor_ordenado = []
    vetor = gera_lista(tamanho)

    print(vetor)

    start = time.time()
    vetor_ordenado = insertion_sort(vetor)
    end = time.time()

    print(vetor_ordenado)
    print('Tempo para ordenacao: ', end - start)

if __name__ == '__main__':
    main()
