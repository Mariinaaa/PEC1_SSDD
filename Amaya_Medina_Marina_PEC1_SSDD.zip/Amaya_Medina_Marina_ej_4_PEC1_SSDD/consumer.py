import rabbitpy
import time

def consumer_thread(queue_name):
    try:
        with rabbitpy.Connection('amqp://guest:guest@localhost:5672/%2F') as connection: #Conectar a RabbitMQ
            with connection.channel() as channel:
                queue = rabbitpy.Queue(channel, queue_name) #Declarar la cola en el canal actual
                queue.declare()  #Crear la cola si no existe

                #Suscribirse al intercambio
                exchange = rabbitpy.Exchange(channel, 'exchange_topic', exchange_type='topic')
                exchange.declare()  #Asegurarse de que el intercambio esté declarado
                queue.bind(exchange, queue_name)  #Vincular la cola al intercambio

                print(f"[CONSUMER] Cola '{queue_name}' creada y suscrita al intercambio 'exchange_topic'")

                while True:
                    print(f"[CONSUMER] Esperando 5 segundos para revisar la cola '{queue_name}'...")
                    time.sleep(5)  #Esperar 5 segundos antes de revisar los mensajes

                    print(f"[CONSUMER] Revisando mensajes en la cola '{queue_name}'...")
                    while True:
                        message = queue.get()  #Obtener un mensaje de la cola
                        if message:
                            print(f"[CONSUMER] Recibido: {message.body.decode()}")
                            message.ack()  #Confirmar que el mensaje fue procesado
                        else:
                            break  #Salir si no hay más mensajes

    except Exception as e:
        print(f"[ERROR] Ocurrió un error en el consumidor: {e}")
