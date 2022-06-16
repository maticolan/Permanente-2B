import time
import random

def INSERTION_SORT(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and key < A[i]:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A


n = 25000
lista = list(range(n))
random.shuffle(lista)


t_inicio = time.time()
l = INSERTION_SORT(lista)
t_final = time.time()
tiempo = t_final - t_inicio
print(f"El tiempo de ejecución del algoritmo Insertion Sort para un n = {n} fue de:",tiempo)