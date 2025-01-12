import random
import time
import threading

stop_propagation = False  #Se usa para detener la difusión si se alcanza el máximo de visitas
lock = threading.Lock()   #Lock para proteger el acceso a recursos compartidos entre hilos

def gossip(node, message, network, visited, max_visits, p_stop, start_node):
    global stop_propagation  #Acceso a la variable global para detener la propagación

    #Inicializa la lista para la propagación en el nodo de inicio
    queue = [node] if node == start_node else []  #Solo el nodo de inicio comienza con el mensaje

    #Mientras haya nodos
    while queue:
        with lock:  #Bloqueo para proteger recursos compartidos
            if stop_propagation:  #Si la propagación debe detenerse
                break  #Sale del bucle y termina la función

            current_node = queue.pop(0) if queue else None  #Toma el siguiente nodo de la lista
            if current_node in visited:  #Si el nodo ya ha sido visitado
                continue  #Salta esta iteración

            visited.add(current_node)  #Marca el nodo actual como visitado
            print(f"Node {current_node} received: {message}")  #Imprime el mensaje recibido para seguimiento

            if len(visited) >= max_visits:  #Si el número de nodos visitados alcanza el límite
                stop_propagation = True  #Detiene la propagación
                break  #Sale del bucle y termina la función

        #Decide si retransmitir el mensaje basado en una probabilidad (p-stop)
        if random.random() < p_stop:  #Si el valor aleatorio es menor que p_stop
            print(f"Node {current_node} ha decidido no retransmitir el rumor (p_stop = {p_stop})")
            continue  #Salta a la siguiente iteración sin retransmitir

        #Selecciona hasta 3 vecinos aleatorios para retransmitir el mensaje
        neighbors = network.get(current_node, [])  #Obtiene los vecinos del nodo actual
        if neighbors:  #Solo si el nodo tiene vecinos
            selected_neighbors = random.sample(neighbors, min(3, len(neighbors)))  #Selecciona hasta 3 vecinos

            #Agrega los vecinos seleccionados a la lista para ser procesados
            with lock:  #Bloqueo para asegurar que no haya conflictos de concurrencia
                for neighbor in selected_neighbors:
                    if neighbor not in visited and not stop_propagation:  #Si el vecino no ha sido visitado
                        queue.append(neighbor)  #Añade el vecino a la lista para procesarlo después

        time.sleep(0.1)  #Pausa breve para simular tiempo de transmisión en la red

#Función principal main
def main():
    #Configuración de los parámetros de la propagación
    start_node = 1  #Nodo desde el cual comienza la difusión
    message = "Important update!"  #Mensaje que se va a propagar
    max_visits = 20  #Número máximo de nodos que deben recibir el mensaje
    p_stop = 0.2     #Probabilidad de que un nodo decida no retransmitir el mensaje

    #Diccionario que representa la red de nodos y sus conexiones
    network = {
        1: [2, 3, 4],
        2: [1, 5, 6],
        3: [1, 7, 8],
        4: [1, 9, 10],
        5: [2, 11, 12],
        6: [2, 13],
        7: [3, 14],
        8: [3, 15],
        9: [4],
        10: [4],
        11: [5],
        12: [5],
        13: [6],
        14: [7],
        15: [8]
    }

    visited = set()  #Para almacenar los nodos que ya han recibido el mensaje
    threads = []  #Lista para almacenar todos los hilos creados

    for node in network.keys():
        #Crea un hilo para ejecutar la función gossip con los argumentos necesarios
        thread = threading.Thread(target=gossip, args=(node, message, network, visited, max_visits, p_stop, start_node))
        threads.append(thread)  #Agrega el hilo a la lista de hilos
        thread.start()  #Inicia el hilo para que empiece a ejecutar

    #Esperar a que todos los hilos terminen su ejecución
    for thread in threads:
        thread.join()  #Espera a que cada hilo en la lista de hilos termine

    #Imprime el número total de nodos alcanzados
    print(f"El mensaje ha llegado a {len(visited)} nodos de {max_visits}.")  #Imprime el resultado final

#Punto de entrada del programa
if __name__ == "__main__":
    main()  #Llama a la función principal para iniciar la simulación
