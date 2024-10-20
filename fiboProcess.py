import multiprocessing
from time import time

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

def calcula_fibonacci(posicion, valor):
    resultado = fibo(valor)
    print(f"Fibonacci de {valor} en la posición {posicion} es {resultado}")

def run_once():

    vector = [33] * 144

    procesos = []

    inicio = time()

    for i in range(len(vector)):
        proceso = multiprocessing.Process(target=calcula_fibonacci, args=(i, vector[i]))
        procesos.append(proceso)
        proceso.start() 
    for proceso in procesos:
        proceso.join()

    fin = time()

    return fin - inicio

def main():
    runs = 5
    execution_times = []

    for run_num in range(runs):
        execution_time = run_once()
        execution_times.append(execution_time)
        print(f"Ejecución {run_num + 1}: {execution_time:.4f} segundos")

    execution_times.sort()
    recortado_times = execution_times[1:-1]

    average_time = sum(recortado_times) / len(recortado_times)
    print(f"Promedio de las ejecuciones (sin el mayor y el menor tiempo): {average_time:.4f} segundos")

if __name__ == "__main__":
    main()
