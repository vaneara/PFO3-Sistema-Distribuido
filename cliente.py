
import socket
import json

HOST = "127.0.0.1"
PUERTO = 5000


def enviar_tarea(operacion, a, b):
    tarea = {
        "operacion": operacion,
        "a": a,
        "b": b
    }

    mensaje = json.dumps(tarea)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((HOST, PUERTO))
        cliente.sendall(mensaje.encode("utf-8"))

        datos = cliente.recv(1024)
        respuesta = json.loads(datos.decode("utf-8"))

    
    print(f"Tarea enviada: {tarea}")

    if "resultado" in respuesta:
        print(f"Resultado recibido: {respuesta['resultado']}")
    else:
        print(f"Error recibido: {respuesta['error']}")

    print("-" * 35)


if __name__ == "__main__":
    enviar_tarea("sumar", 10, 5)
    enviar_tarea("restar", 10, 5)
    enviar_tarea("multiplicar", 10, 5)
    enviar_tarea("dividir", 10, 5)