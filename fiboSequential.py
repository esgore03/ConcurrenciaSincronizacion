import time

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

def calFibo():
    lista = []
    for i in range(12):
        lista.append(i)  
        resultado = fibo(lista[i])  
        print(f"Fibonacci de {lista[i]} es {resultado}")

def measure_execution_time():

    runs = 5
    execution_times = []

    for run_num in range(runs):
        start_time = time.time()  
        calFibo()  
        end_time = time.time()  

        execution_time = end_time - start_time
        execution_times.append(execution_time)
        print(f"Ejecución {run_num + 1}: {execution_time:.4f} segundos")

    execution_times.sort()
    recortado_times = execution_times[1:-1]

    average_time = sum(recortado_times) / len(recortado_times)
    print(f"Promedio de las ejecuciones (sin el mayor y el menor tiempo): {average_time:.4f} segundos")

def main():
    measure_execution_time()

if __name__ == "__main__":
    main()
