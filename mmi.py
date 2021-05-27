T = int(input())

for t in range (T):

    notas = input().split(" ")

    menor = min([int(e) for e in notas])
    maior = max([int(i) for i in notas])
    print(menor, maior)

    if len(set(notas)) == 1:
        print("S", end="" if t == T - 1 else "\n")
    else:
        print("N", end="" if t == T - 1 else "\n")