import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split

# Carregar o dataset Iris
iris = load_iris()
X, y = iris.data, iris.target  # X são as features, y são as classes verdadeiras

# Dividir os dados em 75% treino e 25% teste, com aleatorização
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, shuffle=True)

# Criar e treinar o modelo KMeans com 3 clusters (Iris tem 3 classes)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_train)

# Fazer previsões nos dados de teste
y_pred = kmeans.predict(X_test)

# Criar a matriz de confusão
conf_matrix = confusion_matrix(y_test, y_pred, labels=[0, 1, 2])

# Ajustar a matriz de confusão para o mapeamento correto (como KMeans não possui rótulos exatos)
# Isso pode ser necessário devido à atribuição aleatória de clusters.
from scipy.optimize import linear_sum_assignment

# Reordenar os clusters com base em uma correspondência ótima (Hungarian algorithm)
row_ind, col_ind = linear_sum_assignment(-conf_matrix)
conf_matrix = conf_matrix[:, col_ind]

# Plotar a matriz de confusão corrigida
disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=iris.target_names)
disp.plot(cmap=plt.cm.Blues)

# Exibir o gráfico
plt.title("Matriz de Confusão - KMeans (Iris Dataset)")
plt.show()
