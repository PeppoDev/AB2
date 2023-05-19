import pandas as pd
import numpy as np

data = pd.read_csv("./assets/StudentsPerformance.csv")


# gerador de amostra variando com o tamanho passado e o dataset
# amostra buscada usando aleatoriedade
def sample(items: pd.DataFrame, size: int):
    return items.sample(size)


# filtro por gênero e gerador de amostra
def get_sample_by_gender(gender: str):
    gender_map = data.query(f'gender == @gender')
    gender_map = sample(gender_map, 100)
    return gender_map


# calculo da média baseado na coluna passada
def mean_calc(items: pd.DataFrame, label: str):
    mean = np.mean(items[label])
    return mean

# calculo do desvio padrão baseado na coluna passada
def standard_deviation(items: pd.DataFrame, label: str):
    stdv = items[label].std()
    return stdv


# função que printa todas as informações baseadas na coluna passada
def print_statistics_by_label(items: pd.DataFrame, label: str):
    mean = mean_calc(items, label)
    stdv = standard_deviation(items, label)

    print(f"""{'-'*50}
    {label}
    
    média = {mean}
    desvio_padrao = {stdv}
    tamanho_da_amostra = {len(items)}
    """)


# função que printa todas as informações baseadas no gênero passado
def print_statistics_by_gender(gender: str):
    sample = get_sample_by_gender(gender)

    print(f"""{'-'*50}
    gender = {gender}
          """)

    print_statistics_by_label(sample, 'math score')
    print_statistics_by_label(sample, 'writing score')
    print_statistics_by_label(sample, 'reading score')


# main
print_statistics_by_gender("male")
print_statistics_by_gender("female")
