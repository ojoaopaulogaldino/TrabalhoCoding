# Meu Bolso - Controle Financeiro Pessoal

Aplicativo de terminal feito em Python para controle financeiro pessoal. Permite registrar receitas e despesas, ver saldo e extrato, acompanhar o resumo por categoria e remover lançamentos.

Desenvolvido para a atividade prática de criação de aplicativo em Python (linha de comando), usando funções (`def`), parâmetros, retorno de valores, condicionais (`if/elif/else`) e laços (`while`).

## Funcionalidades

1. **Registrar receita:** adiciona uma entrada com descrição, valor e categoria.
2. **Registrar despesa:** adiciona um gasto com descrição, valor e categoria (da lista ou personalizada).
3. **Consultar saldo e extrato:** mostra todos os lançamentos cadastrados, total de receitas, total de despesas e saldo atual.
4. **Resumo por categoria:** soma receitas e despesas por categoria e mostra o percentual de cada uma.
5. **Remover lançamento:** lista os registros e permite excluir pelo número.

## Como executar

É necessário ter o Python 3 instalado (não usa bibliotecas externas).

```bash
git clone https://github.com/ojoaopaulogaldino/TrabalhoCoding.git
cd TrabalhoCoding
python controle_financeiro.py
```

## Exemplo do menu

```text
==============================================
       MEU BOLSO - CONTROLE FINANCEIRO
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
