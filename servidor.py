
import socket
import json
from concurrent.futures import ThreadPoolExecutor

HOST = "127.0.0.1"
PUERTO = 5000

CANTIDAD_WORKERS = 3
CANTIDAD_CONEXIONES = 10



def procesar_tarea(tarea):
    operacion = tarea.get("operacion")

    try:
        a = tarea["a"]
        b = tarea["b"]

        if not isinstance(a, (int, float)) or isinstance(a, bool):
            return "Error: el primer valor debe ser numérico"

        if not isinstance(b, (int, float)) or isinstance(b, bool):
            return "Error: el segundo valor debe ser numérico"

        if operacion == "sumar":
            return a + b

        elif operacion == "restar":
            return a - b

        elif operacion == "multiplicar":
            return a * b

        else:
            return "Error: operación no reconocida"

    except KeyError:
        return "Error: faltan los valores a o b"




def atender_cliente(conexion, direccion, pool_tareas):
    print(f"Cliente conectado: {direccion}")

    try:
        with conexion:
            datos = conexion.recv(1024)

            if not datos:
                return

            try:
                tarea = json.loads(datos.decode("utf-8"))
            except (json.JSONDecodeError, UnicodeDecodeError):
                respuesta = {"error": "El mensaje debe ser JSON válido"}
                conexion.sendall(json.dumps(respuesta).encode("utf-8"))
                return

            if not isinstance(tarea, dict):
                respuesta = {"error": "La tarea debe ser un objeto JSON"}
                conexion.sendall(json.dumps(respuesta).encode("utf-8"))
                return

            print(f"Tarea recibida de {direccion}: {tarea}")

            futuro = pool_tareas.submit(procesar_tarea, tarea)
            resultado = futuro.result()

            if isinstance(resultado, str) and resultado.startswith("Error:"):
                respuesta = {"error": resultado}
            else:
                respuesta = {"resultado": resultado}

            conexion.sendall(json.dumps(respuesta).encode("utf-8"))
            print(f"Respuesta enviada a {direccion}: {respuesta}")

    except (OSError, ValueError) as error:
        print(f"Error con {direccion}: {error}")



def iniciar_servidor():
    with ThreadPoolExecutor(max_workers=CANTIDAD_WORKERS) as pool_tareas:
        with ThreadPoolExecutor(max_workers=CANTIDAD_CONEXIONES) as pool_conexiones:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
                servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                servidor.bind((HOST, PUERTO))
                servidor.listen()

                print(f"Servidor escuchando en {HOST}:{PUERTO}")
                print(f"Workers de tareas: {CANTIDAD_WORKERS}")
                print(f"Hilos para conexiones: {CANTIDAD_CONEXIONES}")

                while True:
                    conexion, direccion = servidor.accept()

                    pool_conexiones.submit(
                        atender_cliente,
                        conexion,
                        direccion,
                        pool_tareas
                    )


if __name__ == "__main__":
    iniciar_servidor()
