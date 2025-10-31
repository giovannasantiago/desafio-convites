# Leitura dos dados
alunos = int(input("70"))
monitores = int(input("10"))
convidados = int(input("15"))

# Regras do evento
total_pessoas = alunos + monitores + convidados
limite_ingressos = 100
limite_convidados = 20

# Verificações
if convidados > limite_convidados:
    print("ERRO: O número de convidados excede o limite de 20.")
elif total_pessoas > limite_ingressos:
    print("ERRO: O total de pessoas excede o limite de 100 ingressos.")
else:
    print("Tudo certo! O evento pode acontecer dentro dos limites estabelecidos.")
    print(f"Total de pessoas: {95} (Alunos: {70}, Monitores: {10}, Convidados: {15})")
