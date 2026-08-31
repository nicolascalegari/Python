#Simular botao voltar de um navegador

historico = []

historico.append("google.com")
historico.append("youtube.com")
historico.append("github.com")

print(historico)

pagina_anterior = historico.pop()

print("Botão voltar: ", historico[-1])

print("Botão avançar: ", pagina_anterior)