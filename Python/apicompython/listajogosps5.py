jogos = []


jogo1 = {
    "nome": "Grand Theft Auto VI: Ultimate Edition",
    "genero": "Ação, Mundo Aberto, simulação",
    "ano": 2026,
    "plataforma":"Ps5",
    "zerado": False
}

jogo2 = {
    "nome": "007 First Light",
    "genero": "Ação e aventura",
    "ano": 2026,
    "plataforma":"Ps5",
    "zerado": True
}

jogo3 = {
    "nome": "Mafia: The Old Country",
    "genero": "Ação",
    "ano": 2026,
    "plataforma":"Ps5",
    "zerado": True
}

jogo4 = {
    "nome": "Mad Max",
    "genero": "Ação, Mundo Aberto",
    "ano": 2015,
    "plataforma":"Ps4",
    "zerado": False
}

jogo5 = {
    "nome": "A way out",
    "genero": "Ação, Aventura",
    "ano": 2018,
    "plataforma":"Ps4",
    "zerado": False
}

jogo6 = {
    "nome": "It Takes Two",
    "genero": "Aventura",
    "ano": 2021,
    "plataforma":"Ps4, Ps5",
    "zerado": True
}

jogo7 = {
    "nome": "Fifa 26",
    "genero": "Esportes, simulação",
    "ano": 2025,
    "plataforma":"Ps4, Ps5",
    "zerado": False
}

jogo8 = {
    "nome": "Tom Clancy's, The Division",
    "genero": "Ação, Tiro",
    "ano": 2016,
    "plataforma":"Ps4",
    "zerado": False
}

jogo9 = {
    "nome": "Just Cause 4",
    "genero": "Ação, Aventura",
    "ano": 2019,
    "plataforma":"Ps4",
    "zerado": False
}

jogo10 = {
    "nome": "Ride 2",
    "genero": "Direção, Corrida",
    "ano": 2017,
    "plataforma":"Ps4",
    "zerado": False
}

jogo11 = {
    "nome": "Sherlock Holmes: The Devil's Daughter",
    "genero": "Ação, Aventura",
    "ano": 2021,
    "plataforma":"Ps4",
    "zerado": False
}

jogo12 = {
    "nome": "RESIDENT EVIL 7 biohazard",
    "genero": "Ação, Terror",
    "ano": 2022,
    "plataforma":"Ps4, Ps5",
    "zerado": False
}

jogo13 = {
    "nome": "Batman: Arkham Collection",
    "genero": "Ação, Aventura",
    "ano": 2018,
    "plataforma":"Ps4",
    "zerado": True
}

jogo14 = {
    "nome": "Alan Wake Remastered",
    "genero": "Ação",
    "ano": 2021,
    "plataforma":"Ps4, Ps5",
    "zerado": False
}

jogo15 = {
    "nome": "The Witcher 3: Wild Hunter - Remastered",
    "genero": "RPG ação, Mundo Aberto",
    "ano": 2015,
    "plataforma":"Ps4, Ps5",
    "zerado": True
}

jogo16 = {
    "nome": "Mafia: Trilogy",
    "genero": "Ação, Aventura",
    "ano": 2020,
    "plataforma":"Ps4",
    "zerado": True
}

jogo17 = {
    "nome": "Devil My Cry 5",
    "genero": "Ação, Aventura",
    "ano": 2021,
    "plataforma":"Ps4",
    "zerado": True
}

jogo18 = {
    "nome": "Resident Evil 4 PS4 e PS5",
    "genero": "Ação, Aventura, Terror",
    "ano": 2023,
    "plataforma":"Ps4 e Ps5",
    "zerado": True
}

jogos.extend([
    jogo1, jogo2, jogo3, jogo4, jogo5, jogo6,
    jogo7, jogo8, jogo9, jogo10, jogo11, jogo12,
    jogo13, jogo14, jogo15, jogo16, jogo17, jogo18
])

def listar_jogos():
    print("=== MINHA COLEÇÃO DE JOGOS ===")

    print("Total de jogos:", len(jogos))

    total_ps5 = 0

    for jogo in jogos:
        if "Ps5" in jogo["plataforma"]:
            total_ps5 += 1

    print("Total de jogos PS5:", total_ps5)

    for jogo in jogos:
        print("-----------------------")
        print("Nome:", jogo["nome"])
        print("Gênero:", jogo["genero"])
        print("Ano:", jogo["ano"])
        print("Plataforma:", jogo["plataforma"])
        print("Zerado:", jogo["zerado"])

listar_jogos()

def buscar_jogo(nome):
    for jogo in jogos:
        if jogo["nome"].lower() == nome.lower():
            return jogo

    return None

resultado = buscar_jogo("Mad Max")

if resultado:
    print("Jogo encontrado!")
    print("Nome:", resultado["nome"])
    print("Plataforma:", resultado["plataforma"])
else:
    print("Jogo não encontrado!")


def cadastrar_jogo(nome, genero, ano, plataforma, zerado):

    novo_jogo = {
        "nome": nome,
        "genero": genero,
        "ano": ano,
        "plataforma": plataforma,
        "zerado": zerado
    }

    jogos.append(novo_jogo)

    print("Jogo cadastrado com sucesso!")

cadastrar_jogo(
    "Resident Evil ZERO",
    "Ação e terror",
    2026,
    "Ps4, Ps5",
    False
)
print(jogos[-1])