v = int(input())

nota100 = v//100
v %= 100
nota50 = v//50
v %= 50
nota20 = v//20 
v %= 20 
nota10 = v//10
v %= 10
nota5 = v//5
v %= 5
nota2 = v//2
v %= 2
nota1 = v//1
v %= 1

print(f'{nota100} nota(s) de R$ 100')
print(f'{nota50} nota(s) de R$ 50')
print(f'{nota20} nota(s) de R$ 20')
print(f'{nota10} nota(s) de R$ 10')
print(f'{nota5} nota(s) de R$ 5')
print(f'{nota2} nota(s) de R$ 2')
print(f'{nota1} nota(s) de R$ 1', end="")