import random

def valor_carta():
    """Devuelve un valor aleatorio de carta entre 1 y 10."""
    return random.randint(1, 10)

def jugar_blackjack():
    """Función principal para jugar una partida de Blackjack."""
    puntos = 50  # Puntos iniciales del jugador

    while puntos > 0:
        print(f"\nTienes {puntos} puntos.")
        print("Cada partida cuesta 5 puntos.")
        
        if puntos < 5:
            print("No tienes suficientes puntos para jugar. Fin del juego.")
            break
        
        puntos -= 5  # Resta 5 puntos por cada intento de jugar
        total = 0  # Total de puntos de las cartas del jugador

        while True:
            respuesta = input("¿Quieres sacar una carta? (s/n): ").lower()
            
            if respuesta == 's':
                valor = valor_carta()
                print(f"Has sacado una carta con valor: {valor}")
                
                if valor == 1:
                    # Si sacas un As, te pregunta si lo quieres como 1 o 11
                    while True:
                        valor_as = input("¿Quieres que el As valga 1 o 11?: ")
                        if valor_as == '1' or valor_as == '11':
                            valor = int(valor_as)
                            break
                        else:
                            print("Por favor, introduce '1' o '11'.")
                
                total += valor
                print(f"Tu total es: {total}")

                # Si el total supera 21, el jugador pierde 5 puntos
                if total > 21:
                    print("Te has pasado de 21. ¡Pierdes 5 puntos!")
                    puntos -= 5
                    break
                elif total == 21:
                    # Si el total es 21, el jugador gana 100 puntos
                    print("¡Felicidades, has hecho 21! Ganas 100 puntos.")
                    puntos += 100
                    break

            elif respuesta == 'n':
                # Si decide plantarse, muestra el total final y termina la ronda
                print(f"Te has plantado con un total de {total}.")
                break
            else:
                print("Introduce 's' para sacar una carta o 'n' para plantarte.")

        # Si el jugador pierde todos sus puntos, termina el juego
        if puntos <= 0:
            print("¡Has perdido todos tus puntos! Fin del juego.")
            break
        
        # Pregunta si quiere jugar una nueva partida
        while True:
            jugar_nuevo = input(f"¿Quieres jugar otra partida? (Te quedan {puntos} puntos) (s/n): ").lower()
            if jugar_nuevo == 's':
                print("¡Comenzando una nueva partida!")
                break
            elif jugar_nuevo == 'n':
                print(f"¡Fin del juego! Tienes {puntos} puntos acumulados.")
                break
            else:
                print("Por favor, ingresa 's' para jugar de nuevo o 'n' para terminar.")
                continue

if __name__ == "__main__":
    jugar_blackjack()
