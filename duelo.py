import random

# 1. DEFINICAO DAS CARTAS
cartas = {
    "Dragao de Fogo": {
        "Forca": 90,
        "Defesa": 50,
        "Velocidade": 70
    },
    "Guerreiro Ancestral": {
        "Forca": 60,
        "Defesa": 85,
        "Velocidade": 55
    },
    "Mago Sombrio": {
        "Forca": 40,
        "Defesa": 60,
        "Velocidade": 95
    }
}

# 2. INICIO DA PARTIDA
def iniciar_duelo():
    """Escolhe 1 carta para cada jogador."""
    
    lista_cartas = list(cartas.keys())
    duas_cartas = random.sample(lista_cartas, 2)
    
    carta_jogador = duas_cartas[0]
    carta_pc = duas_cartas[1]
    
    return carta_jogador, carta_pc

# 3. LOGICA DO DUELO
def jogar_duelo():
    print("--- BEM-VINDO AO DUELO RAPIDO SUPER TRUNFO! ---")
    
    carta_jogador, carta_pc = iniciar_duelo()
    
    print(f"\nSua carta e: {carta_jogador}")
    
    atributos = list(cartas[carta_jogador].keys())
    print("\nAtributos da sua carta:")
    for i, atributo in enumerate(atributos):
        valor = cartas[carta_jogador][atributo]
        print(f"({i+1}) {atributo}: {valor}")

    # Pede a escolha
    while True:
        try:
            escolha = int(input(f"\nEscolha o numero do atributo para comparar (1 a {len(atributos)}): ")) - 1
            if 0 <= escolha < len(atributos):
                atributo_escolhido = atributos[escolha]
                break
            else:
                print("Escolha invalida. Tente novamente.")
        except ValueError:
            print("Entrada invalida. Digite um numero.")

    # 4. COMPARACAO
    valor_jogador = cartas[carta_jogador][atributo_escolhido]
    valor_pc = cartas[carta_pc][atributo_escolhido]
    
    print("\n--- RESULTADO ---")
    print(f"Voce escolheu {atributo_escolhido}.")
    print(f"Sua carta ({carta_jogador}) tem {atributo_escolhido}: {valor_jogador}")
    print(f"Carta do PC ({carta_pc}) tem {atributo_escolhido}: {valor_pc}")
    
    # 5. VERIFICA O VENCEDOR
    if valor_jogador > valor_pc:
        print("\nVITORIA! Sua carta é superior.")
    elif valor_pc > valor_jogador:
        print("\nDERROTA! A carta do PC era mais forte.")
    else:
        print("\nEMPATE! Os valores sãoo iguais.")

# Executa o jogo
if __name__ == "__main__":
    jogar_duelo()
