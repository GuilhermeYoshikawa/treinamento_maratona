T = int(input())

for t in range (T):

    raio = input().split(" ")

    raio_ovini = int(raio[0]) + int(raio[1])
    raio_plataforma = int(raio[2])

    if (raio_ovini <= raio_plataforma):
        print("CABE!", end="" if t == T - 1 else "\n")
    else:
        print("NAO CABE!", end="" if t == T - 1 else "\n")