from data_loader import carregar_transacoes, carregar_json
from financeiro import calcular_saldo, total_gastos, gastos_por_categoria
from recomendador import recomendar_investimentos

# carregar dados
transacoes = carregar_transacoes("../data/transacoes.csv")
perfil = carregar_json("../data/perfil_investidor.json")
produtos = carregar_json("../data/produtos_financeiros.json")

print("=== Nexus Finance Bot ===\n")

while True:
    comando = input("Digite um comando: ")

    if comando == "saldo":
        saldo = calcular_saldo(transacoes)
        print(f"Seu saldo é: R$ {saldo:.2f}")

    elif comando == "gastos":
        total = total_gastos(transacoes)
        print(f"Total gasto: R$ {total:.2f}")

    elif comando == "categoria":
        categorias = gastos_por_categoria(transacoes)
        for c, v in categorias.items():
            print(f"{c}: R$ {v:.2f}")

    elif comando == "investir":
        rec = recomendar_investimentos(perfil, produtos)
        print("Sugestões:", ", ".join(rec))

    elif comando == "sair":
        break

    else:
        print("Comando não reconhecido.")
