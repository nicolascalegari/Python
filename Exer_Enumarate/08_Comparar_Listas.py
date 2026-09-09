gabarito = ["A", "B", "C", "D"]
respostas = ["A", "B", "C", "E"]

for indice, resposta in enumerate(respostas):

    questao = indice + 1

    if resposta == gabarito[indice]:

        print(f"Questão {questao}: acertou!")

    else:
        print(f"Questão {questao}: errou. Resposta correta era {gabarito[indice]}")