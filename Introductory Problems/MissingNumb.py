n = int(input())
listaA = [int(x) for x in range(1,n+1)]
listaB = [int(x) for x in input().split()]
 
sortedB = sorted(listaB)

cond = False
for i in range(0,len(sortedB)):
    #Condição para sair do loop i
    if cond:
        break
    
    for j in range(i,len(listaA)):
        #Se os dois numeros da lista forem iguais ele quebra o loop de j
        if listaA[j] == sortedB[i]:
            break
        
        #Se for diferente, ele printar o numero que falta na listaB e quebra os dois loops
        else:
            cond = True
            print(listaA[j])
            break

#Essa condição existe pq o for vai até n-1 e não pega o último número
if cond == False:
    print(listaA[n - 1])