import random

def jugar_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]

    while True:
        # Elige una opción para el jugador
        jugador = input("Elige piedra, papel o tijera (o 'salir' para terminar el juego): ").lower()

        # Salir del juego si el jugador lo desea
        if jugador == "salir":
            print("¡Hasta luego!")
            break

        # Verificar la elección del jugador
        if jugador not in opciones:
            print("Elección no válida. Por favor, elige piedra, papel o tijera.")
            continue

        # Generar la elección de la computadora
        computadora = random.choice(opciones)

        # Mostrar las elecciones
        print(f"Jugador eligió: {jugador}")
        print(f"Computadora eligió: {computadora}")

        # Determinar el resultado
        if jugador == computadora:
            print("¡Empate!")
        elif (jugador == "piedra" and computadora == "tijera") or (jugador == "papel" and computadora == "piedra") or (jugador == "tijera" and computadora == "papel"):
            print("¡Jugador gana!")
        else:
            print("¡Computadora gana!")

if __name__ == "__main__":
    jugar_piedra_papel_tijera()
