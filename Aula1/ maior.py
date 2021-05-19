entrada = input().split(" ")
a = int (entrada[0])
b = int (entrada[1])
c = int (entrada[2])
maior = (a + b + abs(a - b)) // 2
maior2 = (c + maior + abs(maior-c)) // 2
print(maior2, end="")