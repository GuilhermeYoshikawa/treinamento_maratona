#for i in range (3):
#   print (i)

#for i in range (3, 10, 2):
#    print (i)

#for i in range (10):
#    print (i)
#    if i == 5:
#        break # interrompe

#for i in range (10):
#    if i == 5:
#        continue # pula apenas o número 5
#    print (i)

#for i in range (10):
#    print (i)
#else:
#    print ("Saindo do for. Valor do i: " + str(i))

#for i in range (1, 10):
#    print (i)
#    if i % 3 == 0:
#        break
#    else:
#        print ("Saindo do for: Valor do i: " + str(1))

#for i in enumerate (range(10, 20)):
#    print(i)

for tupla in enumerate (range(10, 20)):
    print(tupla[0])
    print(tupla[1]) 

#tupla unpacking
for indice, valor in  enumerate (range(10, 20)):
    print (valor)

lista = [1, 2, 3, 4, 5]
lista.append(7)
lista = lista + [3]

for elemento in lista:
    print (elemento)

lista = [1, 4.5, 'Texto', True]
for e in lista:
    print (e)

#list comprehensions
lista = [x ** 2 for x in [1, 2]]
print (lista)

lista = [x + y for x in [1, 2, 3] for y in [4, 5, 6]]
print (lista)