import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from kneed import KneeLocator
import random

# Função para gerar 1000 pontos aleatórios em 2D
def gerar_dataset(num_pontos=1000, escala=100):
    return [[random.uniform(0, escala), random.uniform(0, escala)] for _ in range(num_pontos)]

# Passo 1: Carregar o conjunto de dados Iris
#iris_data = load_iris()
#X = iris_data.data  # Recursos
X=gerar_dataset(1000, escala=255)
# Calcular a inércia para diferentes números de clusters
inertias = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)
# Encontrar o número de clusters usando o KneeLocator
kneedle = KneeLocator(range(1, 11), inertias, curve='convex', direction='decreasing')
elbow_number = kneedle.elbow

print("Número de clusters no elbow:", elbow_number)


# Plotar o gráfico da inércia em relação ao número de clusters
plt.plot(range(1, 11), inertias, marker='o')
plt.xlabel('Número de clusters')
plt.ylabel('Inércia')
plt.title('Método Elbow para o Dataset ')
plt.xticks(range(1, 11))
plt.show()

#agora, utilizando Método da Calinski-Harabasz
#(índice de variação entre clusters)
#Este método calcula a razão entre a dispersão dentro dos clusters e a dispersão entre os clusters.
#Um valor mais alto indica clusters mais densos e bem separados.
#O número ideal de clusters é aquele que maximiza este índice.

from sklearn.metrics import calinski_harabasz_score
# Calcular o índice de variação entre clusters para diferentes números de clusters
scores = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    score = calinski_harabasz_score(X, kmeans.labels_)
    scores.append(score)
plt.plot(range(2, 11), scores, marker='o')
plt.xlabel('Número de clusters')
plt.ylabel('Scores')
plt.title('Método Calinski-Harabasz para o Dataset ')
plt.xticks(range(2, 11))
x=np.argmax(scores)
plt.text(x, scores[x], 'Escolher maior scores', color='red', fontsize=12, fontweight='bold')

plt.show()
# Encontrar o número de clusters com o maior índice de variação entre clusters
optimal_num_clusters = np.argmax(scores) + 2  # +2 porque começamos a partir de k=2

print("Número ótimo de clusters pela Calinski-Harabasz:", optimal_num_clusters)

