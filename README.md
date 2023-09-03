# MI PRIMER PROYECTO DE PHYTON 
## _Curso de CodeSpace 2023_

El juego de **Piedra, Papel y Tijera** es un juego clásico en el que dos jugadores eligen entre tres opciones posibles: piedra, papel o tijera. El objetivo del juego es vencer al oponente eligiendo una opción que sea superior a la elección del oponente. Las reglas son simples:

- **Piedra vence a Tijera**: Si un jugador elige piedra y el otro elige tijera, la piedra gana porque puede romper la tijera.

- **Tijera vence a Papel**: Si un jugador elige tijera y el otro elige papel, las tijeras ganan al cortar el papel.

- **Papel vence a Piedra**: Si un jugador elige papel y el otro elige piedra, el papel gana al envolver la piedra.

- Si ambos jugadores eligen la misma opción, el juego es un **empate** y se juega otra ronda.

## Cómo funciona el programa

El programa de Python que hemos creado es una implementación básica del juego de Piedra, Papel y Tijera. Aquí está el funcionamiento del programa:

1. **Elección de opciones**: El programa permite al jugador elegir entre las tres opciones posibles: piedra, papel o tijera. También proporciona la opción de "salir" para terminar el juego.

2. **Validación de la entrada del jugador**: El programa verifica si la entrada del jugador es válida. Si el jugador ingresa algo que no sea una de las opciones válidas, se le pide que elija nuevamente.

3. **Elección de la computadora**: El programa genera una elección aleatoria para la computadora entre las tres opciones.

4. **Comparación de elecciones**: El programa compara la elección del jugador con la elección de la computadora según las reglas del juego para determinar el resultado.

5. **Mostrar el resultado**: El programa muestra las elecciones del jugador y la computadora, y anuncia si el jugador gana, pierde o hay un empate.

6. **Repetición o salida**: Después de mostrar el resultado, el programa ofrece la opción de jugar otra ronda o salir del juego.

El juego continúa hasta que el jugador decide salir del juego ingresando "salir".

## Cómo ejecutar el programa

Para ejecutar el programa, asegúrate de tener Python instalado en tu computadora. Luego, guarda el código en un archivo con extensión ".py" y ejecútalo desde la línea de comandos o una IDE de Python.

```bash
python Main.py
