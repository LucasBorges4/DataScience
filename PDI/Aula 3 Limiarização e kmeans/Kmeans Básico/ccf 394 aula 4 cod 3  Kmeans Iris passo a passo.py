'''
import random
import math

import random
import math
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score



def distancia_euclidiana(ponto1, ponto2):
    soma_quadrados = sum([(ponto1[i] - ponto2[i]) ** 2 for i in range(len(ponto1))])
    return math.sqrt(soma_quadrados)

def inicializar_centroides(dataset, k):
    centroides = random.sample(dataset, k)
    return centroides

def criar_clusters(dataset, centroides):
    clusters = [[] for _ in range(len(centroides))]
    for ponto in dataset:
        distancia_minima = float('inf')
        cluster_atual = None
        for i, centroide in enumerate(centroides):
            distancia = distancia_euclidiana(ponto, centroide)
            if distancia < distancia_minima:
                distancia_minima = distancia
                cluster_atual = i
        clusters[cluster_atual].append(ponto)
    return clusters

def calcular_media(cluster):
    num_atributos = len(cluster[0])
    media = [0] * num_atributos
    for ponto in cluster:
        for i in range(num_atributos):
            media[i] += ponto[i]
    media = [m / len(cluster) for m in media]
    return media

def atualizar_centroides(clusters):
    centroides = [calcular_media(cluster) for cluster in clusters]
    
    # Plota os dados
    plt.clf()
    cores = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i in range(len(clusters)):
        for ponto in clusters[i]:
            plt.scatter(ponto[0], ponto[1], c=cores[i])
        if len(clusters[i]) > 0:
            plt.scatter(centroides[i][0], centroides[i][1], c=cores[-i-1], marker='x')
    plt.pause(1)
    print("1")
    
    return centroides

def diferenca_centroides(centroides1, centroides2):
    if centroides1 is None or centroides2 is None:
        return float('inf')
    return sum([distancia_euclidiana(centroides1[i], centroides2[i]) for i in range(len(centroides1))])

def kmeans(dataset, k):
    centroides = inicializar_centroides(dataset, k)
    centroides_antigos = None
    while centroides_antigos is None or diferenca_centroides(centroides, centroides_antigos) > 0:
        clusters = criar_clusters(dataset, centroides)
        centroides_antigos = centroides
        centroides = atualizar_centroides(clusters)
        diferenca = diferenca_centroides(centroides, centroides_antigos) if centroides_antigos is not None else float('inf')
    return clusters

# Carregar conjunto de dados Iris
iris = load_iris()

# Executa o algoritmo K-Means no dataset Iris
k = 3
centroides = kmeans(iris, k)
'''
import random
import math
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Função para calcular a distância euclidiana entre dois pontos
def distancia_euclidiana(ponto1, ponto2):
    soma_quadrados = sum([(ponto1[i] - ponto2[i]) ** 2 for i in range(len(ponto1))])
    return math.sqrt(soma_quadrados)

# Inicializar os centroides escolhendo k amostras aleatórias do dataset
def inicializar_centroides(dataset, k):
    indices = random.sample(range(len(dataset)), k)  # Selecionar índices aleatórios
    return [dataset[i] for i in indices]

# Criar clusters associando cada ponto ao centroide mais próximo
def criar_clusters(dataset, centroides):
    clusters = [[] for _ in range(len(centroides))]
    for ponto in dataset:
        distancia_minima = float('inf')
        cluster_atual = None
        for i, centroide in enumerate(centroides):
            distancia = distancia_euclidiana(ponto, centroide)
            if distancia < distancia_minima:
                distancia_minima = distancia
                cluster_atual = i
        clusters[cluster_atual].append(ponto)
    return clusters

# Calcular a média de cada cluster para obter novos centroides
def calcular_media(cluster):
    num_atributos = len(cluster[0])
    media = [0] * num_atributos
    for ponto in cluster:
        for i in range(num_atributos):
            media[i] += ponto[i]
    media = [m / len(cluster) for m in media]
    return media

# Atualizar os centroides e plotar os dados (2D)
def atualizar_centroides(clusters):
    centroides = [calcular_media(cluster) for cluster in clusters]
    
    # Plotar os clusters e os centroides
    plt.clf()
    cores = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i in range(len(clusters)):
        for ponto in clusters[i]:
            plt.scatter(ponto[0], ponto[1], c=cores[i])
        if len(clusters[i]) > 0:
            plt.scatter(centroides[i][0], centroides[i][1], c=cores[-i-1], marker='X')
    plt.pause(1)
    
    return centroides

# Calcular a diferença entre os centroides antigos e novos
def diferenca_centroides(centroides1, centroides2):
    if centroides1 is None or centroides2 is None:
        return float('inf')
    return sum([distancia_euclidiana(centroides1[i], centroides2[i]) for i in range(len(centroides1))])

# Algoritmo K-Means
def kmeans(dataset, k):
    centroides = inicializar_centroides(dataset, k)
    centroides_antigos = None
    while centroides_antigos is None or diferenca_centroides(centroides, centroides_antigos) > 0:
        clusters = criar_clusters(dataset, centroides)
        centroides_antigos = centroides
        centroides = atualizar_centroides(clusters)
    return clusters

# Carregar conjunto de dados Iris e trabalhar com apenas 2 atributos (para visualização 2D)
iris = load_iris()
data = iris.data[:, :2]  # Pegando apenas os 2 primeiros atributos para visualização (sepal length e width)

# Executar o algoritmo K-Means no dataset Iris
k = 5
plt.ion()  # Ativar modo interativo para plotar dinamicamente
clusters = kmeans(data, k)
plt.ioff()
plt.show()

