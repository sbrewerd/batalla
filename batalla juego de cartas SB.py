import random


pintas = ['treboles', 'diamantes', 'picas', 'corazones']
cartas = [f"{numero} de {pinta}" for pinta in pintas for numero in range(1, 14)]

random.shuffle(cartas)

mazo = []
puntos_jugador = 0
puntos_computadora = 0


while cartas:
    input("presiona enter para repartir la siguiente carta ")
    
    
    carta_actual = cartas.pop(0)
    mazo.append(carta_actual)
    

    print(f"la carta es: {carta_actual}")
    
    
    if cartas:
        siguiente_carta = cartas[0]
        if siguiente_carta.split()[0] == carta_actual.split()[0]:
            respuesta = input("batalla! quieres jugar? (escribe 'batalla' para jugar): ")
            if respuesta.lower() == 'batalla':
                puntos_jugador += 1
                print("punto para el jugador!")
            else:
                puntos_computadora += 1
                print("batalla!")
    

print(f"Puntos del jugador: {puntos_jugador}")
print(f"Puntos de la computadora: {puntos_computadora}")

if puntos_jugador > puntos_computadora:
    print("¡El jugador gana!")
elif puntos_computadora > puntos_jugador:
    print("¡La computadora gana!")
else:
    print("¡Es un empate!")
