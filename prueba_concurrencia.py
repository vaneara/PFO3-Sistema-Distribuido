
import socket
import json
from concurrent.futures import ThreadPoolExecutor

HOST = "127.0.0.1"
PUERTO = 5000


def enviar_tarea(numero):
    tarea = {
        "operacion": "sumar",
        "a": numero,
        "b": 100
    }

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((HOST, PUERTO))
        cliente.sendall(json.dumps(tarea).encode("utf-8"))

        datos = cliente.recv(1024)
        respuesta = json.loads(datos.decode("utf-8"))

    print(f"Cliente {numero}: resultado = {respuesta['resultado']}")


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as pool:
        pool.map(enviar_tarea, range(1, 6))
