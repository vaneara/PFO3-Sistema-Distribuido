# PFO 3 — Sistema Distribuido Cliente-Servidor
# Aracena Vanesa 3°E

## Descripción

Este proyecto implementa un sistema cliente-servidor en Python mediante sockets TCP. El cliente envía tareas al servidor en formato JSON y recibe una respuesta con el resultado del procesamiento.

El servidor utiliza un pool de hilos para atender conexiones concurrentes y otro pool para procesar las tareas recibidas.

## Tecnologías utilizadas

- Python 3.14
- Sockets TCP
- JSON para el intercambio de datos
- ThreadPoolExecutor para la gestión de hilos

## Estructura del proyecto

- `servidor.py`: recibe conexiones, valida solicitudes y distribuye tareas para su procesamiento.
- `cliente.py`: envía tareas y muestra los resultados recibidos.
- `prueba_concurrencia.py`: permite probar varias conexiones de clientes en paralelo.

## Operaciones disponibles

- Sumar dos números.
- Restar dos números.
- Multiplicar dos números.

El servidor también contempla operaciones desconocidas y solicitudes con datos inválidos.

## Ejecución

### 1. Iniciar el servidor

Abrir una terminal en la carpeta del proyecto y ejecutar:

```bash
python servidor.py
```

El servidor escucha en `127.0.0.1`, puerto `5000`.

### 2. Ejecutar el cliente

Abrir una segunda terminal y ejecutar:

```bash
python cliente.py
```

### 3. Probar concurrencia

Con el servidor activo, ejecutar:

```bash
python prueba_concurrencia.py
```

La prueba envía cinco tareas desde clientes concurrentes y muestra los resultados recibidos.

