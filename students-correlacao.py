'''
Alunos:
Ruan Víctor Barros Nunes - 19111177
Felyphe Henrick Nicacio da Silva - 19111472
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("./assets/StudentsPerformance.csv")

# funçao de renderizacao do grafico de disperssao baseado em duas colunas
def render_graph(variables: list, labels: list):
    plt.scatter(variables[0], variables[1])
    plt.xlabel(f"{labels[0]}")
    plt.ylabel(f"{labels[0]}")
    plt.title(f"Relação entre {labels[0]} e {labels[1]}")
    plt.show()

# calculador do coeficiente de correlação linear
def correlation_coeficient(data: pd.DataFrame, labelx: str, labely: str):
    correlation = np.corrcoef(data[labelx], data[labely])[0, 1]
    return correlation


# print de todas as informações baseadas nas colunas passadas
def print_infos_by_labels(data: pd.DataFrame, labelx: str, labely: str):
    value = correlation_coeficient(data, labelx, labely)
    print(f"""{"-"*50}
    Coeficiente de correlação linear entre {labelx} e {labely} é {value}
    """)

    render_graph([data[labelx], data[labely]], [labelx, labely])


print_infos_by_labels(data, "math score", "writing score")
print_infos_by_labels(data, "math score", "reading score")
print_infos_by_labels(data, "reading score", "writing score")
