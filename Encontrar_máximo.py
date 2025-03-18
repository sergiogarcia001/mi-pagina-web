#Lista
lista = []
while True:
    numero = int(input(f"Introduce un número (0 para finalizar):"))
    if numero == 0:
        break
    lista.append(numero)
    
#Encontrar_Máximo
if lista:
    print(f"El valor máximo de la lista es: {max(lista)}")