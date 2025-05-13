import numpy as np 
import pandas as pd
from sklearn.decomposition import PCA
from sklearn import datasets
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#plt.style.use('seaborn')
# importa dataset IRIS
iris = datasets.load_iris()
# cria um objeto df com os dados e caracteristicas do dataset IRIS
df = pd.DataFrame(data=iris['data'],columns=iris['feature_names'])
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
print(df.head())
'''
g=sns.pairplot(data=df,kind='scatter', hue='species')
import matplotlib.pyplot as plt
plt.show()
'''
# teste
arr=df.to_numpy()

arr=arr[:,0:3]
fig = plt.figure(figsize=(18, 10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(arr[:,0], arr[:,1],arr[:,2], c=iris.target, s=100,cmap = 'viridis')
ax.view_init(20, 90)
plt.title("Antes PCA")
plt.show()


import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn import datasets
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('seaborn')

# Importa o dataset Iris
iris = datasets.load_iris()

# Cria um DataFrame com os dados e características do dataset Iris
df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

print(df.head())

# Plota a matriz de dispersão antes da PCA
g = sns.pairplot(data=df, kind='scatter', hue='species')
plt.show()

# Prepara os dados para PCA
X = df.iloc[:, 0:4]  # Seleciona todas as linhas das colunas 0 até 4

# Aplica PCA para reduzir para 2 componentes principais
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Cria um DataFrame com os dados transformados e as classes
df_pca = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
df_pca['species'] = df['species']

# Plota a separação das classes após PCA
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_pca, x='PC1', y='PC2', hue='species', palette='viridis', s=100)
plt.title('Separação das Classes após PCA (2 Componentes Principais)')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.legend(title='Espécie')
plt.show()

# Se quiser plotar os 3 primeiros componentes principais em 3D
pca_3d = PCA(n_components=3)
X_pca_3d = pca_3d.fit_transform(X)

fig = plt.figure(figsize=(18, 10))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(X_pca_3d[:, 0], X_pca_3d[:, 1], X_pca_3d[:, 2], c=iris.target, s=100, cmap='viridis')
ax.set_xlabel('Componente Principal 1')
ax.set_ylabel('Componente Principal 2')
ax.set_zlabel('Componente Principal 3')
ax.set_title('Separação das Classes após PCA (3 Componentes Principais)')

# Adiciona a legenda manualmente
handles, labels = scatter.legend_elements(prop="colors")
ax.legend(handles, iris.target_names, title='Espécie')

plt.show()

# Exibe a variância explicada e os valores singulares
print("Variância Explicada por Componente:\n", pca.explained_variance_ratio_)
print("Valores Singulares:\n", pca.singular_values_)

# Apresenta os loading scores para os 2 primeiros componentes principais
loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

# Cria um DataFrame com os loading scores
loading_df = pd.DataFrame(data=loadings, columns=['PC1', 'PC2'], index=df.columns[:-1])
print("Loading Scores para os 2 primeiros Componentes Principais:\n", loading_df)

# Se estiver usando PCA com 3 componentes principais
loadings_3d = pca_3d.components_.T * np.sqrt(pca_3d.explained_variance_)

# Cria um DataFrame com os loading scores
loading_df_3d = pd.DataFrame(data=loadings_3d, columns=['PC1', 'PC2', 'PC3'], index=df.columns[:-1])
print("Loading Scores para os 3 primeiros Componentes Principais:\n", loading_df_3d)
