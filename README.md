# PEC1_SSDD

Este repositorio contiene 4 ejercicios prácticos que abordan conceptos clave en sistemas distribuidos.

## Ejercicios:

### Ejercicio 1: Actualización de una variable compartida con hilos
Simula la actualización de una variable compartida llamada `counter` a través de varios hilos. Este ejercicio permite observar cómo los hilos interactúan con una variable global sin sincronización adecuada.

### Ejercicio 2: Protocolo de Gossip (propagación de rumores)
Implementa un modelo básico del **protocolo de Gossip** en Python. Los nodos de la red propagan un mensaje a sus vecinos, con una probabilidad de no retransmitir el mensaje. La propagación se detiene cuando un número máximo de nodos ha recibido el mensaje.

### Ejercicio 3: Reloj lógico vectorial
Implementa un **reloj lógico vectorial** en un sistema distribuido. Cada nodo mantiene un vector de tiempos y lo actualiza a medida que se procesan eventos. Este reloj asegura un orden causal entre eventos distribuidos.

### Ejercicio 4: Sistema de mensajería Emisor-Suscriptor con AMQP
Implementa un modelo **Emisor-Suscriptor** utilizando **AMQP**, donde los productores publican mensajes en diferentes **topics** (como "sports", "news", "weather") y los consumidores se suscriben a estos temas para recibir los mensajes.

## Requisitos

- **Python 3.8+**
- **RabbitMQ** (Para el Ejercicio 4)

### Librerías:
- `threading`
- `random`
- `time`
- `rabbitpy` (para RabbitMQ)

## Instalación de dependencias
pip install rabbitpy
