def combinar(numeros, tamanho, atual = []):

    if len(atual) == tamanho:
        print(atual)
        return
    
    for numero in numeros:

        if numero not in atual:
            atual.append(numero)
            combinar(numeros, tamanho, atual)
            atual.pop()
            
combinar([1,2,3], 2)