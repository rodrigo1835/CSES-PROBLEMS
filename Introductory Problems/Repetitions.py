string = input()
lista = [1] #A maior sequencia é 1
chr_last = '' 
n = 1 

#Um for que vai passar por cada carectere na minha string 
for i in string:
    #Compara se o caractere anterior é igual ao atual
    #Se for ele vai somar +1 e guardar dentro de uma lista
    if chr_last == i:
        n += 1
        lista.append(n)
    
    #Se a variavel a for diferente do carectere n
    #Ele vai resetar a variavel n pra um
    else:
        n = 1
    
    #A variavel chr_last vai armazernar o valor anterior de i
    chr_last = i

#Printa o maior valor de n que eu armazenei na lista
print(max(lista))