from datetime import datetime

CATEGORIAS_RECEITA = ["Salário", "Freelance", "Investimentos", "Presente", "Outros"]
CATEGORIAS_DESPESA = [
    "Alimentação",
    "Moradia",
    "Transporte",
    "Saúde",
    "Educação",
    "Lazer",
    "Outros",
]


# Formata um número para o formato R$ 0,00
def formatar_moeda(valor):
    texto = f"{abs(valor):.2f}".replace(".", ",")
    if valor < 0:
        return f"-R$ {texto}"
    return f"R$ {texto}"


def ler_valor_positivo(mensagem):
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(entrada)
            if valor > 0:
                return valor
            print("Digite um valor maior que zero.")
        except ValueError:
            print("Valor inválido. Tente algo como 150.50 ou 150,50.")


def escolher_categoria(tipo):
    if tipo == "receita":
        categorias = CATEGORIAS_RECEITA
    else:
        categorias = CATEGORIAS_DESPESA

    print("\nCategorias disponíveis:")
    for i in range(len(categorias)):
        print(f"  {i + 1}. {categorias[i]}")
    print(f"  {len(categorias) + 1}. Digitar outra categoria")

    while True:
        escolha = input("Escolha o número da categoria: ").strip()
        if escolha.isdigit():
            numero = int(escolha)
            if 1 <= numero <= len(categorias):
                return categorias[numero - 1]
            elif numero == len(categorias) + 1:
                personalizada = input("Digite o nome da categoria: ").strip()
                if personalizada != "":
                    return personalizada
                print("A categoria não pode ficar vazia.")
            else:
                print("Número fora das opções.")
        else:
            print("Digite apenas o número da categoria.")


def exibir_menu():
    print("\n==============================================")
    print("       MEU BOLSO - CONTROLE FINANCEIRO")
    print("==============================================")
    print("1. Registrar receita")
    print("2. Registrar despesa")
    print("3. Consultar saldo e extrato")
    print("4. Resumo por categoria")
    print("5. Remover lançamento")
    print("6. Sair")
    print("==============================================")


# Função base usada para cadastrar receita ou despesa
def registrar_transacao(transacoes, tipo):
    if tipo == "receita":
        titulo = "RECEITA"
    else:
        titulo = "DESPESA"

    print(f"\n--- REGISTRAR NOVA {titulo} ---")

    while True:
        descricao = input("Descrição (ex: Salário, Mercado, Luz): ").strip()
        if descricao != "":
            break
        print("A descrição não pode ficar vazia.")

    valor = ler_valor_positivo("Valor (R$): ")
    categoria = escolher_categoria(tipo)
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")

    nova_transacao = {
        "data": data_atual,
        "tipo": tipo,
        "descricao": descricao,
        "categoria": categoria,
        "valor": valor,
    }

    transacoes.append(nova_transacao)
    print(f"\n{titulo.capitalize()} registrada: {descricao} ({formatar_moeda(valor)})")
    return nova_transacao


def registrar_receita(transacoes):
    return registrar_transacao(transacoes, "receita")


def registrar_despesa(transacoes):
    return registrar_transacao(transacoes, "despesa")


def calcular_resumo(transacoes):
    total_receitas = 0.0
    total_despesas = 0.0

    for item in transacoes:
        if item["tipo"] == "receita":
            total_receitas += item["valor"]
        elif item["tipo"] == "despesa":
            total_despesas += item["valor"]

    saldo = total_receitas - total_despesas
    return total_receitas, total_despesas, saldo


def consultar_saldo_e_extrato(transacoes):
    print("\n--- SALDO E EXTRATO ---")

    if len(transacoes) == 0:
        print("Nenhum lançamento registrado ainda.")
        return

    for i in range(len(transacoes)):
        item = transacoes[i]
        if item["tipo"] == "receita":
            tipo_texto = "Receita"
            sinal = "+"
        else:
            tipo_texto = "Despesa"
            sinal = "-"

        print(
            f"{i + 1}. [{item['data']}] {tipo_texto} | {item['categoria']} | "
            f"{item['descricao']} | {sinal} {formatar_moeda(item['valor'])}"
        )

    total_receitas, total_despesas, saldo = calcular_resumo(transacoes)

    print("\n----------------------------------------------")
    print(f"Total de receitas: {formatar_moeda(total_receitas)}")
    print(f"Total de despesas: {formatar_moeda(total_despesas)}")
    print(f"Saldo atual: {formatar_moeda(saldo)}")

    if saldo > 0:
        print("Situação: Saldo positivo!")
    elif saldo < 0:
        print("Situação: Atenção, saldo negativo.")
    else:
        print("Situação: Saldo zerado.")


# Agrupa os valores por categoria e mostra o percentual de cada uma
def exibir_resumo_por_categoria(transacoes):
    print("\n--- RESUMO POR CATEGORIA ---")

    if len(transacoes) == 0:
        print("Nenhum lançamento registrado para gerar resumo.")
        return

    receitas_cat = {}
    despesas_cat = {}

    for item in transacoes:
        categoria = item["categoria"]
        valor = item["valor"]
        if item["tipo"] == "receita":
            if categoria in receitas_cat:
                receitas_cat[categoria] += valor
            else:
                receitas_cat[categoria] = valor
        elif item["tipo"] == "despesa":
            if categoria in despesas_cat:
                despesas_cat[categoria] += valor
            else:
                despesas_cat[categoria] = valor

    total_receitas, total_despesas, _ = calcular_resumo(transacoes)

    print("\nReceitas por categoria:")
    if len(receitas_cat) > 0:
        for categoria, valor in receitas_cat.items():
            if total_receitas > 0:
                percentual = (valor / total_receitas) * 100
            else:
                percentual = 0
            print(f"  - {categoria}: {formatar_moeda(valor)} ({percentual:.1f}%)")
    else:
        print("  Nenhuma receita cadastrada.")

    print("\nDespesas por categoria:")
    if len(despesas_cat) > 0:
        for categoria, valor in despesas_cat.items():
            if total_despesas > 0:
                percentual = (valor / total_despesas) * 100
            else:
                percentual = 0
            print(f"  - {categoria}: {formatar_moeda(valor)} ({percentual:.1f}%)")
    else:
        print("  Nenhuma despesa cadastrada.")


def remover_transacao(transacoes):
    print("\n--- REMOVER LANÇAMENTO ---")

    if len(transacoes) == 0:
        print("Não há lançamentos para remover.")
        return False

    for i in range(len(transacoes)):
        item = transacoes[i]
        if item["tipo"] == "receita":
            tipo_texto = "Receita"
        else:
            tipo_texto = "Despesa"

        print(
            f"  {i + 1}. [{item['data']}] {tipo_texto} - "
            f"{item['descricao']} ({item['categoria']}) | {formatar_moeda(item['valor'])}"
        )

    while True:
        escolha = input("\nDigite o número do lançamento para remover (ou 0 para cancelar): ").strip()
        if not escolha.isdigit():
            print("Digite um número válido.")
            continue

        numero = int(escolha)
        if numero == 0:
            print("Remoção cancelada.")
            return False
        elif 1 <= numero <= len(transacoes):
            removido = transacoes.pop(numero - 1)
            print(f"Lançamento removido: {removido['descricao']} ({formatar_moeda(removido['valor'])})")
            return True
        else:
            print("Número de lançamento inexistente.")


def main():
    transacoes = []
    print("Bem-vindo ao MEU BOLSO!")

    executando = True
    while executando:
        exibir_menu()
        opcao = input("Escolha uma opção (1 a 6): ").strip()

        if opcao == "1":
            registrar_receita(transacoes)
        elif opcao == "2":
            registrar_despesa(transacoes)
        elif opcao == "3":
            consultar_saldo_e_extrato(transacoes)
        elif opcao == "4":
            exibir_resumo_por_categoria(transacoes)
        elif opcao == "5":
            remover_transacao(transacoes)
        elif opcao == "6":
            print("\nObrigado por usar o MEU BOLSO! Até logo.")
            executando = False
        else:
            print("\nOpção inválida! Escolha um número entre 1 e 6.")


main()
