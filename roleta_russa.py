import random
import time

def roleta_russa():
    print("Bem-vindo à Roleta Russa")
    print("Um tambor com 6 espaços... 1 está carregado.\n")


    bala = random.randint(0, 5)

    input("Pressione ENTER para girar o tambor...")
    print("Girando...")
    time.sleep(1)


    disparo = random.randint(0, 5)

    input("Pressione ENTER para puxar o gatilho...")
    print("...")

    time.sleep(1)

    if disparo == bala:
        print("BANG! Você perdeu.")
    else:
        print("Clique! Você sobreviveu.")

if __name__ == "__main__":
    roleta_russa()