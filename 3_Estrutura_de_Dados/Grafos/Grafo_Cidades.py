cidades = {
    "Sao Paulo": ["Campinas", "Santos"],
    "Campinas": ["Sao Paulo", "Ribeirao Preto"],
    "Santos": ["Sao Paulo"],
    "Ribeirao Preto": ["Campinas"]
}

for cidade, conexoes in cidades.items():
    print(cidade, "->", conexoes)