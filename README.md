# Meu Bolso Controle Financeiro Pessoal

Aplicativo de linha de comando (terminal) desenvolvido em **Python** para auxiliar no controle financeiro pessoal do dia a dia, permitindo registrar receitas e despesas, consultar saldo e extrato, analisar gastos por categoria e remover lançamentos.

Projeto desenvolvido para a **Atividade Prática – Criação de Aplicativo em Python (Linha de Comando)**, aplicando modularização com funções (`def`), parâmetros, retorno de valores, estruturas condicionais e laços de repetição.

---

## Funcionalidades

1. **Registrar receita:** cadastra entradas financeiras com descrição, valor (aceitando vírgula ou ponto) e categoria.
2. **Registrar despesa:** cadastra gastos com descrição, valor e categoria (sugerida ou personalizada).
3. **Consultar saldo e extrato:** lista todas as movimentações em formato de tabela, calcula o total de receitas, total de despesas, saldo atual e exibe a situação financeira.
4. **Resumo por categoria:** agrupa receitas e despesas por categoria, exibindo o valor total e o percentual de cada uma.
5. **Remover lançamento:** permite excluir qualquer lançamento cadastrado mediante confirmação pelo número.

---

## Requisitos da atividade atendidos

- **Menu principal:** 5 funcionalidades + opção `6. Sair`.
- **Funções (`def`):** 12 funções organizadas por responsabilidade (`formatar_moeda`, `ler_valor_positivo`, `escolher_categoria`, `exibir_menu`, `registrar_transacao`, `registrar_receita`, `registrar_despesa`, `calcular_resumo`, `consultar_saldo_e_extrato`, `exibir_resumo_por_categoria`, `remover_transacao` e `main`).
- **Modularização:** cada funcionalidade do menu possui sua própria função dedicada.
- **Parâmetros e argumentos:** funções como `registrar_transacao(transacoes, tipo)`, `escolher_categoria(tipo)`, `calcular_resumo(transacoes)` e `formatar_moeda(valor)`.
- **Retorno de valores (`return`):** utilizado em funções como `formatar_moeda`, `ler_valor_positivo`, `escolher_categoria`, `calcular_resumo`, `registrar_transacao` e `remover_transacao`.
- **Estruturas condicionais (`if`, `elif`, `else`):** aplicadas no menu principal, validações de entrada e análise de saldo.
- **Estrutura de repetição (`while`):** mantém o menu principal ativo até a opção de sair e valida entradas do usuário.
- **Entrada e saída (`input()` e `print()`):** toda a interação ocorre diretamente no terminal.

---

## Como executar

### Pré-requisitos
- **Python 3.8 ou superior** instalado (não é necessária nenhuma biblioteca externa).

### Passos
1. Clone o repositório ou baixe os arquivos:
   ```bash
   git clone https://github.com/ojoaopaulogaldino/TrabalhoCoding.git
   cd TrabalhoCoding
   ```
2. Execute o aplicativo no terminal:
   ```bash
   python controle_financeiro.py
   ```

---

## Estrutura do projeto

```text
.
├── controle_financeiro.py   # Código-fonte principal do aplicativo
├── README.md                # Documentação do projeto
└── .gitignore               # Ignora arquivos temporários do Python
```

---

## Exemplo de uso no terminal

```text
==============================================
       MEUBOLSO - CONTROLE FINANCEIRO
==============================================
1. Registrar receita
2. Registrar despesa
3. Consultar saldo e extrato
4. Resumo por categoria
5. Remover lançamento
6. Sair
==============================================
Escolha uma opção (1 a 6):
```
