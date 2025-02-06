import random

def valor_carta():
    
    return random.randint(1, 11) 

def jugar_blackjack():
    puntos = 50  #Puntos iniciales del jugador

    while puntos > 0:
        print(f"\nTienes {puntos} puntos.")
        puntos -= 5  #Valor de cada intento

        total = 0
        while True:
            respuesta = input("¿Quieres sacar una carta? (s/n): ").lower()
            if respuesta == 's':
                valor = valor_carta()
                print(f"Has sacado una carta con valor: {valor}")

                if valor == 1:
                    while True:
                        valor_as = input("¿Quieres que as valga 1 o 11?: ")
                        if valor_as in ['1', '11']:
                            valor = int(valor_as)
                            break
                        else:
                            print("Error. Introduce 1 o 11.")
                
                total += valor
                print(f"Tu total es: {total}")

                if total > 21:
                    print("Te has pasado de 21. ¡Pierdes 5 puntos!")
                    puntos -= 5
                    break
                elif total == 21:
                    print("¡Ganas 100 puntos!")
                    puntos += 100
                    break
            elif respuesta == 'n':
                print(f"Tu total final es: {total}. No has ganado ni perdido puntos.")
                break
            else:
                print("Introduce bien los datos. Introduce 's' o 'n'")

        if puntos <= 0:
            print("¡Has perdido!")
            break
        
        while True:
            jugar_nuevo = input("¿Quieres volver a jugar? (s/n): ").lower()
            if jugar_nuevo == 's':
                print("¡Comenzando un nuevo juego!")
                break  
            elif jugar_nuevo == 'n':
                print("¡Fin del juego!")
                return  
            else:
                print("Por favor, ingresa 's' para jugar de nuevo o 'n' para terminar.")
                continue

if __name__ == "__main__":
    jugar_blackjack()