import threading
import time

# Fibo:
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Trabajadores (Mediante Hilos):
class FiboWorker(threading.Thread):
    def __init__(self, vector, start_index, end_index, tid):
        threading.Thread.__init__(self)
        self.vector = vector
        self.start_index = start_index
        self.end_index = end_index
        self.tid = tid

    def run(self):
        for i in range(self.start_index, self.end_index):
            self.vector[i] = fibonacci(self.vector[i])

# Se ejecutan 5 veces los 144 procesos en 12 hilos.
def main():
    num_threads = 12
    vector_length = 144
    runs = 5
    execution_times = []

    for run_num in range(runs):
        # Inicia siempre con 33:
        vector = [33] * vector_length
        
        # Crea los hilos y los divide en 12:
        threads = []
        step = vector_length // num_threads
        start_time = time.time()

        for i in range(num_threads):
            start_index = i * step
            end_index = start_index + step
            worker = FiboWorker(vector, start_index, end_index, i)
            worker.start()  # Inicia el hilo
            threads.append(worker)

        # Espera a que todos los hilos terminen
        for thread in threads:
            thread.join()

        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
        # Muestra el tiempo de las 5 ejecuciones:
        print(f"Ejecución {run_num + 1}: {execution_time:.4f} segundos")

    # Ordena los tiempos de ejecución y les quita el mayor y el menor:
    execution_times.sort()
    recortado_times = execution_times[1:-1]

    # Calcula el promedio de los tiempos, luego de quitar el mayor y el menor
    average_time = sum(recortado_times) / len(recortado_times)
    print(f"Promedio de las ejecuciones (sin el mayor y el menor tiempo): {average_time:.4f} segundos")

if __name__ == "__main__":
    main()
