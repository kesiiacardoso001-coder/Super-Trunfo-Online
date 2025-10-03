print("=== SUPER TRUNFO SIMPLES ===")

# Atributos do jogador
forca_jogador = 90
defesa_jogador = 50
velocidade_jogador = 70

# Atributos do PC
forca_pc = 60
defesa_pc = 85
velocidade_pc = 55

# Mostra a carta do jogador
print("\nSua carta é: Dragão de Fogo")
print("1 - Força:", forca_jogador)
print("2 - Defesa:", defesa_jogador)
print("3 - Velocidade:", velocidade_jogador)

# Escolha do atributo
escolha = int(input("\nEscolha o número do atributo: "))

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
print("Seu valor:", valor_jogador)
print("PC:", valor_pc)

if valor_jogador > valor_pc:
    print("\nVocê VENCEU!")
elif valor_jogador < valor_pc:
    print("\nVocê PERDEU!")
else:
    print("\nEMPATE!")

