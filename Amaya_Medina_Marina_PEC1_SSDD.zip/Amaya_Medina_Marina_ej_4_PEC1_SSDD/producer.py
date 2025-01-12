import rabbitpy
import time

def producer_thread(producer_name, routing_key, interval=1):
    """Función que representa un hilo productor de mensajes."""
    counter = 0  #Inicializar el contador
    with rabbitpy.Connection('amqp://guest:guest@localhost:5672/%2F') as connection:
        with connection.channel() as channel:
            #Declarar el intercambio de tipo 'topic' llamado 'exchange_topic'
            exchange = rabbitpy.Exchange(channel, 'exchange_topic', exchange_type='topic')
            exchange.declare()

            while True:
                counter += 1  #Incrementar el contador
                message = f"Mensaje {counter} de productor {producer_name} en el topic {routing_key}" #Mensaje con nuestro formato
                #Crear y publicar el mensaje
                msg = rabbitpy.Message(channel, message)
                msg.publish(exchange, routing_key)
                print(f"[PRODUCER] Enviado: '{message}' en el topic '{routing_key}'")
                time.sleep(interval)  #Esperar 1 segundo entre envíos
