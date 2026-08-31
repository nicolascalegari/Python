from collections import deque

impressora = deque()

impressora.append("Trabalho.pdf")
impressora.append("Relatorio.pdf")
impressora.append("Curriculo.pdf")

while impressora:
    documento = impressora.popleft()
    print("Imprimindo: ", documento)