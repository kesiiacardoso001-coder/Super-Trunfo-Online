print("SUPER TRUNFO SIMPLES")

# Atributos do jogador
nome_jogador = "Dragão de Fogo"
forca_jogador = 90
defesa_jogador = 50
velocidade_jogador = 70

# Atributos do PC
nome_pc = "Fênix Azul"
forca_pc = 60
defesa_pc = 85
velocidade_pc = 55

# Mostra a carta do jogador
print(f"\nSua carta é: {nome_jogador}")
print("1 - Força:", forca_jogador)
print("2 - Defesa:", defesa_jogador)
print("3 - Velocidade:", velocidade_jogador)

# Escolha do atributo
escolha = input("\nEscolha o número do atributo: ")

if escolha not in ["1", "2", "3"]:
    print("\nOpção inválida! Escolha apenas 1, 2 ou 3.")
else:
    escolha = int(escolha)
    if escolha == 1:
        atributo = "Força"
        valor_jogador = forca_jogador
        valor_pc = forca_pc
    elif escolha == 2:
        atributo = "Defesa"
        valor_jogador = defesa_jogador
        valor_pc = defesa_pc
    else:
        atributo = "Velocidade"
        valor_jogador = velocidade_jogador
        valor_pc = velocidade_pc

    # Mostra resultado
    print("\n--- RESULTADO ---")
    print("Você escolheu:", atributo)
    print(f"Sua carta: {nome_jogador} - Valor: {valor_jogador}")
    print(f"Carta do PC: {nome_pc} - Valor: {valor_pc}")

    if valor_jogador > valor_pc:
        print("\nVocê VENCEU!")
    elif valor_jogador < valor_pc:
        print("\nVocê PERDEU!")
    else:
        print("\nEMPATE!")
