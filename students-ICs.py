import pandas as pd
import numpy as np
import scipy

data = pd.read_csv("./assets/StudentsPerformance.csv")


def sample(items: pd.DataFrame, size: int):
    return items.sample(size)

# filtro por gênero e gerador de amostra


def get_sample_by_gender(gender: str):
    gender_map = data.query(f'gender == @gender')
    gender_map = sample(gender_map, 100)
    return gender_map


# calculo do intervalo de confiança
def confidence_interval(sample: pd.Series, confidence):
    # normalização do array, não é tão necessário mas evita alguns problemas
    data = np.array(sample)
    # tamanho da amostra
    n = len(data)

    # calculo automático do erro padrão
    standard_error = scipy.stats.sem(data)
    media = np.mean(data)

    # calculo da margem usando ppf
    margem = standard_error * scipy.stats.t.ppf((confidence + 1)/2., n-1)
    # calculo e retorno do intervalo
    return media-margem, media+margem

# função que printa todas as informações baseadas na coluna passada


def print_interval_by_label(sample: pd.DataFrame, label: str):
    percent = 0.95
    ci = confidence_interval(sample[label], 0.95)

    print(f"""
    {label}
    
    intervalo_de_confianca = ({ci[0]}, {ci[1]})
    grau = {percent}
    
    """)


# função que printa todas as informações baseadas no gênero passado
def print_statistics_by_gender(gender: str):
    sample = get_sample_by_gender(gender)

    print(f"""{'-'*50}
    gender = {gender}
          """)

    print_interval_by_label(sample, 'math score')
    print_interval_by_label(sample, 'writing score')
    print_interval_by_label(sample, 'reading score')

    print(f"""{'-'*50}""")


print_statistics_by_gender("male")
print_statistics_by_gender("female")


