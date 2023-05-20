'''
Alunos:
Ruan Víctor Barros Nunes - 19111177
Felyphe Henrick Nicacio da Silva - 19111472
'''

import pandas as pd
import numpy as np
from scipy import stats

# Leitura do arquivo CSV e exibição das primeiras linhas do DataFrame
data = pd.read_csv('assets/StudentsPerformance.csv')

# H0 Media masculina math > IC media femino math
# HA Media masculina math <= IC media femino math


# gerador de amostra variando com o tamanho passado e o dataset
# amostra buscada usando aleatoriedade
def sample(items: pd.DataFrame, size: int):
    return items.sample(size)


# filtro por gênero e gerador de amostra
def get_sample_by_gender(gender: str):
    gender_map = data.query(f'gender == @gender')
    gender_map = sample(gender_map, 100)
    return gender_map


# funcao que calcula o limite superior do intervalo de confiaça da média das notas recebidas
def confidence_interval(sample: pd.Series, confidence):
    # normalização do array, não é tão necessário mas evita alguns problemas
    data = np.array(sample)
    # tamanho da amostra
    n = len(data)

    # calculo automático do erro padrão
    standard_error = stats.sem(data)
    mean = np.mean(data)

    # calculo da margem usando ppf
    margin = standard_error * stats.t.ppf((confidence + 1)/2., n-1)
    # calculo e retorno do intervalo
    return mean+margin

# funcao que calcula a media baseado numa coluna e num dataset passdo


def mean_calc(items: pd.DataFrame, label: str):
    mean = np.mean(items[label])
    return mean


# funcao que calcula o test de hipotese retornando o respectivo veredito recebendo parametros dinamicos relativos as alternativas
def hypothesis_test(gender: str, gender_comparative: str, label: str, alternative: str):
    gender_grades = get_sample_by_gender(gender)[label]
    gender_comparative_grades = get_sample_by_gender(gender_comparative)[label]

    superior_ci = confidence_interval(
        gender_comparative_grades, 0.95)
    size = len(gender_grades)

    # Calculando a estatística de teste t
    t_obs = (np.mean(gender_grades) - superior_ci) / \
        (np.std(gender_grades, ddof=1) / np.sqrt(size))

    # Calculando o valor-p
    value_p = 1 - stats.t.cdf(np.abs(t_obs), df=size-1)
    alpha = 0.05

    if value_p < alpha:
        veredict = f"Rejeitar Hipotese nula pois o valor p ({value_p}) é menor que alpha ({alpha}), logo, a média de {label} para o gênero {gender} é superior ao valor máximo do IC do grupo {gender_comparative}."
    else:
        veredict = f"Não rejeitar a hipótese nula pois o valor p ({value_p}) não é menor que alpha ({alpha}). Portanto,  média de {label} para o gênero {gender} não é superior ao valor máximo do IC do grupo {gender_comparative}."

    print(f"""{"-"*50}
       Alternativa: {alternative}
    """)
    print(veredict)


# main
hypothesis_test("male", "female", "math score", "A")
hypothesis_test("female", "male", "reading score", "B")
hypothesis_test("female", "male", "writing score", "C")
