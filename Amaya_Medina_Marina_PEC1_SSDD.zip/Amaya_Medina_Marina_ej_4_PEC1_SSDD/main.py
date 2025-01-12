#docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
import threading
from producer import producer_thread
from consumer import consumer_thread
import sys

def main():
    while True:
        #Mostrar un menú simple para elegir entre productor, consumidor o salir
        print("\nMenu:")
        print("1. Enviar mensajes (Productor)")
        print("2. Recibir mensajes (Consumidor)")
        print("3. Salir")
        
        #Solicitar al usuario que elija una opción
        choice = input("Selecciona una opción (1, 2, o 3): ")
        
        if choice == '1':
            #Solicitar el nombre del productor y el tema (topic) de mensajes
            producer_name = input("Introduce el nombre del productor: ")
            topic = input("Introduce el topic: ")
            
            #Crear e iniciar un hilo productor
            producer = threading.Thread(target=producer_thread, args=(producer_name, topic, 1))
            producer.start()  #Iniciar el hilo productor
            
            print(f"[INFO] Productor '{producer_name}' enviando mensajes en el topic '{topic}'...")
            
            #Mantener el programa en ejecución mientras el productor sigue enviando mensajes
            producer.join()  #Esperar a que el hilo termine (no terminará en este caso)

        elif choice == '2':
            #Solicitar al usuario el tema (topic) al que desea suscribirse
            topic = input("Introduce el topic a suscribirse: ")
            
            #Crear e iniciar un hilo consumidor
            consumer = threading.Thread(target=consumer_thread, args=(topic,))
            consumer.start()  #Iniciar el hilo consumidor
            
            print(f"[INFO] Consumidor suscrito al topic '{topic}'...")

            #Mantener el programa en ejecución mientras el consumidor sigue recibiendo mensajes
            consumer.join()  #Esperar a que el hilo termine (no terminará en este caso)

        elif choice == '3':
            #Salir del programa
            print("Saliendo del programa...")
            sys.exit()
            break  #Romper el bucle y finalizar el programa

        else:
            #Informar al usuario si la opción seleccionada no es válida y repetir el menú
            print("Opción no válida, por favor intenta de nuevo.")

#Ejecutar la función main si se ejecuta el script directamente
if __name__ == "__main__":
    main()
