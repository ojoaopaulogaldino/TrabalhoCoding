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


def formatar_moeda(valor):
    #Formata um número float para o padrão monetário brasileiro (R$).#
    sinal = "-" if valor < 0 else ""
    valor_formatado = f"{abs(valor):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{sinal}R$ {valor_formatado}"


def ler_valor_positivo(mensagem):
    #Solicita ao usuário um valor numérico maior que zero e retorna como float.#
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(entrada)
            if valor > 0:
                return valor
            print("Digite um valor maior que zero.")
        except ValueError:
            print("Valor inválido. Exemplo válido: 150.50 ou 150,50.")


def escolher_categoria(tipo):
    #Permite escolher uma categoria sugerida ou digitar uma categoria personalizada.#
    if tipo == "receita":
        categorias = CATEGORIAS_RECEITA
    else:
        categorias = CATEGORIAS_DESPESA

    print("\nCategorias disponíveis:")
    for indice, nome in enumerate(categorias, start=1):
        print(f"  {indice}. {nome}")
    print(f"  {len(categorias) + 1}. Digitar outra categoria")

    while True:
        escolha = input("Escolha o número da categoria: ").strip()
        if escolha.isdigit():
            numero = int(escolha)
            if 1 <= numero <= len(categorias):
                return categorias[numero - 1]
            elif numero == len(categorias) + 1:
                personalizada = input("Digite o nome da categoria: ").strip()
                if personalizada:
                    return personalizada
                print("A categoria não pode ficar vazia.")
            else:
                print("Número fora das opções disponíveis.")
        else:
            print("Digite apenas o número correspondente à categoria.")


def exibir_menu():
    #Exibe o menu principal do aplicativo no terminal.#
    print("\n" + "=" * 46)
    print("       MEU BOLSO-CONTROLE FINANCEIRO")
    print("=" * 46)
    print("1. Registrar receita")
    print("2. Registrar despesa")
    print("3. Consultar saldo e extrato")
    print("4. Resumo por categoria")
    print("5. Remover lançamento")
    print("6. Sair")
    print("=" * 46)


def registrar_transacao(transacoes, tipo):
    #Registra uma nova transação (receita ou despesa) e retorna o registro criado.#
    titulo = "RECEITA" if tipo == "receita" else "DESPESA"
    print(f"\n--- REGISTRAR NOVA {titulo} ---")

    while True:
        descricao = input("Descrição (ex: Salário, Mercado, Luz): ").strip()
        if descricao:
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
    print(f"\n{titulo.capitalize()} registrada com sucesso: {descricao} ({formatar_moeda(valor)})")
    return nova_transacao


def registrar_receita(transacoes):
    #Funcionalidade de registro de receita.#
    return registrar_transacao(transacoes, "receita")


def registrar_despesa(transacoes):
    #Funcionalidade de registro de despesa.#
    return registrar_transacao(transacoes, "despesa")


def calcular_resumo(transacoes):
    #Calcula e retorna o total de receitas, o total de despesas e o saldo atual.#
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
    #Exibe todas as movimentações cadastradas e o resumo financeiro atual.#
    print("\n--- SALDO E EXTRATO ---")

    if not transacoes:
        print("Nenhum lançamento registrado até o momento.")
        return

    print(f"{'Nº':<4} {'Data':<17} {'Tipo':<9} {'Categoria':<15} {'Descrição':<20} {'Valor':>14}")
    print("-" * 83)

    for indice, item in enumerate(transacoes, start=1):
        tipo_texto = "Receita" if item["tipo"] == "receita" else "Despesa"
        valor_texto = formatar_moeda(item["valor"])
        if item["tipo"] == "receita":
            valor_exibido = f"+ {valor_texto}"
        else:
            valor_exibido = f"- {valor_texto}"

        descricao_curta = item["descricao"][:19]
        categoria_curta = item["categoria"][:14]
        print(
            f"{indice:<4} {item['data']:<17} {tipo_texto:<9} "
            f"{categoria_curta:<15} {descricao_curta:<20} {valor_exibido:>14}"
        )

    total_receitas, total_despesas, saldo = calcular_resumo(transacoes)

    print("-" * 83)
    print(f"Total de receitas: {formatar_moeda(total_receitas)}")
    print(f"Total de despesas: {formatar_moeda(total_despesas)}")
    print(f"Saldo atual:       {formatar_moeda(saldo)}")

    if saldo > 0:
        print("Situação:          Saldo positivo!")
    elif saldo < 0:
        print("Situação:          Atenção! Saldo negativo.")
    else:
        print("Situação:          Saldo zerado (receitas iguais às despesas).")


def exibir_resumo_por_categoria(transacoes):
    #Agrupa e exibe o total de receitas e despesas por categoria.#
    print("\n--- RESUMO POR CATEGORIA ---")

    if not transacoes:
        print("Nenhum lançamento registrado para gerar resumo.")
        return

    receitas_cat = {}
    despesas_cat = {}

    for item in transacoes:
        categoria = item["categoria"]
        valor = item["valor"]
        if item["tipo"] == "receita":
            receitas_cat[categoria] = receitas_cat.get(categoria, 0.0) + valor
        elif item["tipo"] == "despesa":
            despesas_cat[categoria] = despesas_cat.get(categoria, 0.0) + valor

    total_receitas, total_despesas, _ = calcular_resumo(transacoes)

    print("\nReceitas por categoria:")
    if receitas_cat:
        for categoria, valor in sorted(receitas_cat.items(), key=lambda x: x[1], reverse=True):
            percentual = (valor / total_receitas) * 100 if total_receitas > 0 else 0
            print(f"  - {categoria:<18}: {formatar_moeda(valor):>14} ({percentual:.1f}%)")
    else:
        print("  Nenhuma receita cadastrada.")

    print("\nDespesas por categoria:")
    if despesas_cat:
        for categoria, valor in sorted(despesas_cat.items(), key=lambda x: x[1], reverse=True):
            percentual = (valor / total_despesas) * 100 if total_despesas > 0 else 0
            print(f"  - {categoria:<18}: {formatar_moeda(valor):>14} ({percentual:.1f}%)")
    else:
        print("  Nenhuma despesa cadastrada.")


def remover_transacao(transacoes):
    #Remove um lançamento escolhido pelo usuário e retorna True se algum item foi removido.#
    print("\n--- REMOVER LANÇAMENTO ---")

    if not transacoes:
        print("Não há lançamentos para remover.")
        return False

    for indice, item in enumerate(transacoes, start=1):
        tipo_texto = "Receita" if item["tipo"] == "receita" else "Despesa"
        print(
            f"  {indice}. [{item['data']}] {tipo_texto} - "
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
            print(
                f"Lançamento removido: {removido['descricao']} "
                f"({formatar_moeda(removido['valor'])})"
            )
            return True
        else:
            print("Número de lançamento inexistente.")


def main():
    #Função principal que controla o fluxo do menu interativo.#
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


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nPrograma encerrado pelo usuário.")
