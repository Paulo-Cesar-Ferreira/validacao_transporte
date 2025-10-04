# Capacidade máxima do veículo
capacidade_peso = 1000  # em kg
capacidade_passageiros = 5  # número de pessoas

# Dados da carga e passageiros que desejam ser transportados
peso_carga = float(input("Digite o peso total da carga (kg): "))
num_passageiros = int(input("Digite o número de passageiros: "))

print("\n--- Validação de Transporte ---")

# Verificando o peso
if peso_carga > capacidade_peso:
    print(f"❌ O peso da carga ({peso_carga} kg) ultrapassa o limite de {capacidade_peso} kg.")
else:
    print(f"✅ O peso da carga ({peso_carga} kg) está dentro do limite de {capacidade_peso} kg.")

# Verificando a quantidade de passageiros
if num_passageiros > capacidade_passageiros:
    print(f"❌ O número de passageiros ({num_passageiros}) ultrapassa o limite de {capacidade_passageiros}.")
else:
    print(f"✅ O número de passageiros ({num_passageiros}) está dentro do limite de {capacidade_passageiros}.")

# Decisão final
if peso_carga <= capacidade_peso and num_passageiros <= capacidade_passageiros:
    print("\n🚚 O transporte está APROVADO! Pode seguir viagem.")
else:
    print("\n⚠️ O transporte foi NEGADO! Reveja peso ou passageiros.")
