import pandas as pd
import numpy as np
from scipy import stats

# Leitura do arquivo CSV e exibição das primeiras linhas do DataFrame
df = pd.read_csv('assets/StudentsPerformance.csv')
df.head()

# Filtragem dos dados para o gênero masculino e feminino
male = df.loc[df['gender'] == 'male']
female = df.loc[df['gender'] == 'female']

# Função para calcular o intervalo de confiança


def intervalo_confianca(data, nivel_confianca=0.95):
    media_dados = np.mean(data)
    desvio_padrao = np.std(data, ddof=1)
    n = len(data)
    t_critico = stats.t.ppf((1 + nivel_confianca) / 2, df=n-1)
    margem_erro = t_critico * desvio_padrao / np.sqrt(n)
    intervalo_confianca = (media_dados - margem_erro,
                           media_dados + margem_erro)
    return intervalo_confianca


'''Função para realizar o teste de hipótese para notas de matemática para verificar se a média de notas em matemática
para o gênero masculino é superior ao valor máximo do IC da média de notas em matemática
para o gênero feminino'''
# ALTERNATIVA A


def teste_hipotese_genero_matematica_notas(notas_masculino, IC_feminino, alpha=0.05):
    tamanho = len(notas_masculino)
    t_obs = (np.mean(notas_masculino) -
             IC_feminino[1]) / (np.std(notas_masculino, ddof=1) / np.sqrt(tamanho))
    p_valor = 1 - stats.t.cdf(np.abs(t_obs), df=tamanho-1)
    if p_valor < alpha:
        decisao = "Rejeitar H0. A média de notas em matemática para o gênero masculino é superior ao valor máximo do IC do grupo feminino."
    else:
        decisao = "Não rejeitar H0. Não há evidência estatística de que a média de notas em matemática para o gênero masculino seja superior ao valor máximo do IC do grupo feminino."
    return decisao


# Impressão do resultado do teste de hipótese para notas de matemática do gênero masculino
print('Alternativa A')
print(teste_hipotese_genero_matematica_notas(
    notas_masculino=male['math score'].values, IC_feminino=intervalo_confianca(data=female['math score'])), '\n')

'''Função para realizar o teste de hipótese para notas de leitura do gênero feminino para verificar se a média de notas em leitura para
o gênero feminino é superior ao valor máximo do IC da média de notas em leitura para o gênero masculino'''
# ALTERNATIVA B


def teste_hipotese_genero_leitura_notas(notas_feminino, IC_masculino, alpha=0.05):
    tamanho = len(notas_feminino)
    t_obs = (np.mean(notas_feminino) -
             IC_masculino[1]) / (np.std(notas_feminino, ddof=1) / np.sqrt(tamanho))
    p_valor = 1 - stats.t.cdf(np.abs(t_obs), df=tamanho-1)
    if p_valor < alpha:
        decisao = "Rejeitar H0. A média de notas em leitura para o gênero feminino é superior ao valor máximo do IC do grupo masculino."
    else:
        decisao = "Não rejeitar H0. Não há evidência estatística de que a média de notas em leitura para o gênero feminino seja superior ao valor máximo do IC do grupo masculino."
    return decisao


# Impressão do resultado do teste de hipótese para notas de leitura do gênero feminino
print('Alternativa B')
print(teste_hipotese_genero_leitura_notas(
    notas_feminino=female['math score'].values, IC_masculino=intervalo_confianca(data=male['math score'])), '\n')

'''Função para realizar o teste de hipótese para notas de escrita do gênero feminino para verificar se a média de notas em escrita para
o gênero feminino é superior ao valor máximo do IC da média de notas em escrita para o gênero masculino'''
# ALTERNATIVA C


def teste_hipotese_genero_escrita_notas(notas_feminino, IC_masculino, alpha=0.05):
    tamanho = len(notas_feminino)
    t_obs = (np.mean(notas_feminino) -
             IC_masculino[1]) / (np.std(notas_feminino, ddof=1) / np.sqrt(tamanho))
    p_valor = 1 - stats.t.cdf(np.abs(t_obs), df=tamanho-1)
    if p_valor < alpha:
        decisao = "Rejeitar H0. A média de notas em escrita para o gênero feminino é superior ao valor máximo do IC do grupo masculino."
    else:
        decisao = "Não rejeitar H0. Não há evidência estatística de que a média de notas em escrita para o gênero feminino seja superior ao valor máximo do IC do grupo masculino."
    return decisao


# Impressão do resultado do teste de hipótese para notas de escrita do gênero feminino
print('Alternativa C')
print(teste_hipotese_genero_escrita_notas(
    notas_feminino=female['math score'].values, IC_masculino=intervalo_confianca(data=male['math score'])), '\n')
