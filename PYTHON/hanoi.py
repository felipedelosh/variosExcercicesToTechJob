"""
Torres de hanoi DeepSeek
"""
def torres_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
    else:
        torres_hanoi(n - 1, origen, auxiliar, destino)
        print(f"Mover disco {n} de {origen} a {destino}")
        torres_hanoi(n - 1, auxiliar, destino, origen)


n = 3
torres_hanoi(n, "A", "B", "C")
