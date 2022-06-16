import random
import time

def BUBBLESORT(L):
    n = len(L)
    for i in range(0, n):
        for j in range(n-1, i, -1):
            if L[j] < L[j-1]:
                key = L[j]
                L[j] = L[j-1]
                L[j-1] = key
                
    return L

n = 25000

lista = list(range(n))
random.shuffle(lista)
t1 = time.time()
l = BUBBLESORT(lista)
t2 = time.time()
t_final = t2-t1


print(f"El tiempo de ejecución del algoritmo Bubble Sort para un n = {n} fue de:",t_final)