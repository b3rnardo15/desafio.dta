import pandas as pd
import numpy as np
import os


def criar_dados_excel(nome_arquivo):
    # Cria um DataFrame com os dados de exemplo
    # e salva em um arquivo Excel
    data = {
        "Região": ["Norte", "Norte", "Sul", "Sul", "Norte"],
        "Mês": ["Jan", "Fev", "Jan", "Fev", "Mar"],
        "Vendas": [1500, np.nan, 2200, 1800, 2000],
        "Despesas": [300, 250, np.nan, 400, 350]
    }

    df = pd.DataFrame(data)
    df.to_excel(nome_arquivo, index=False, engine="openpyxl")
    print(f"\nArquivo '{nome_arquivo}' criado com sucesso.")


def carregar_dados(nome_arquivo):
    # Lê os dados do arquivo Excel e exibe suas informações básicas
    df = pd.read_excel(nome_arquivo)
    print("\nDados carregados do arquivo:")
    print(df)
    print("\nInformações do DataFrame:")
    print(df.info())
    return df


def tratar_dados(df):
    # Substitui valores ausentes em 'Vendas' com a mediana da coluna
    median_vendas = df["Vendas"].median()
    df["Vendas"] = df["Vendas"].fillna(median_vendas)

    # Substitui valores ausentes em 'Despesas' com a média da coluna
    mean_despesas = df["Despesas"].mean()
    df["Despesas"] = df["Despesas"].fillna(mean_despesas)

    print("\nDados após substituição de valores ausentes:")
    print(df)
    return df


def gerar_agrupamentos(df):
    # Agrupa os dados por Região e Mês, calculando a soma das vendas
    soma_vendas = df.groupby(["Região", "Mês"])["Vendas"].sum()
    print("\nSoma total de vendas por região e mês:")
    print(soma_vendas)

    # Calcula a média das despesas por Região e Mês
    media_despesas = df.groupby(["Região", "Mês"])["Despesas"].mean()
    print("\nMédia de despesas por região e mês:")
    print(media_despesas)


def combinar_colunas(df):
    # Cria um novo DataFrame com apenas as colunas Vendas e Despesas
    df_combinado = pd.concat([df["Vendas"], df["Despesas"]], axis=1)
    print("\nDataFrame com colunas Vendas e Despesas combinadas:")
    print(df_combinado)


def gerar_sumario(df):
    # Exibe estatísticas descritivas para as colunas numéricas
    print("\nSumário estatístico para colunas numéricas:")
    print(df.describe())


def main():
    # Função principal: executa todas as etapas do processamento
    nome_arquivo = input("Digite o nome do arquivo Excel (ex: vendas.xlsx): ").strip()
    
    criar_dados_excel(nome_arquivo)
    
    df = carregar_dados(nome_arquivo)
    df = tratar_dados(df)
    
    gerar_agrupamentos(df)
    combinar_colunas(df)
    gerar_sumario(df)


if __name__ == "__main__":
    main()


