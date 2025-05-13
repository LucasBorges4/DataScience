import cv2
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import classification_report
import seaborn as sns
import matplotlib.pyplot as plt

def extrair_caracteristicas_imagem(caminho_imagem, tamanho_patch=50):
    imagem = cv2.imread(caminho_imagem)
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    caracteristicas = []
    labels = []

    for linha in range(18): #São 18 linhas
        for coluna in range(20):  #Cada linha com 20 figuras
            y = linha * 50
            x = coluna * 50

            patch = imagem[y:y+tamanho_patch, x:x+tamanho_patch] #tamanho 50x50

            vetor_patch = patch.flatten()
            caracteristicas.append(vetor_patch)

            if linha < 6:                    #¨primeiras 6 linhas circulo, e assim sucessivamente
                labels.append('circulo')
            elif linha < 12:
                labels.append('quadrado')
            else:
                labels.append('triangulo')

    return caracteristicas, labels


caracteristicas, labels = extrair_caracteristicas_imagem('prova1_2024_treinamento.png')
print(f"Quantidade de elementos: {len(caracteristicas)}")
print(f"Tamanho de cada elementos {(len(caracteristicas[0]))}")
print("\n\n")
# Contar o número de ocorrências de cada classe para verificação
contagem_classes = pd.Series(labels).value_counts()

print("Número de amostras por classe:")
print(contagem_classes)


df = pd.DataFrame(caracteristicas)
df['Classe'] = labels

X = df.drop('Classe', axis=1)
Y = df['Classe']

# Dividir os dados em conjunto de treinamento e conjunto de teste 50% pra cada 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)


svm = SVC(kernel='linear')
svm.fit(X_train, Y_train)

Y_pred = svm.predict(X_test)

# Exibir relatório de classificação e acurácia
print("Relatório de Classificação:")
print(classification_report(Y_test, Y_pred))

accuracy = accuracy_score(Y_test, Y_pred)
print(f"Acurácia: {accuracy*100:.2f} %")


# Calcular e exibir a matriz de confusão
conf_matrix = confusion_matrix(Y_test, Y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=svm.classes_, yticklabels=svm.classes_)
plt.xlabel('Rótulos previstos')
plt.ylabel('Rótulos verdadeiros')
plt.title('Matriz de Confusão')
plt.show()

imagem = cv2.imread('prova1_2024_busca.png')

# Escala de cores HSV
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Definir o intervalo de cor vermelha na escala HSV
vermelho_baixo = np.array([0, 50, 50])
vermelho_alto = np.array([10, 255, 255])
vermelho_mascara_baixa = cv2.inRange(imagem_hsv, vermelho_baixo, vermelho_alto)

vermelho_baixo = np.array([170, 50, 50])
vermelho_alto = np.array([180, 255, 255])
vermelho_mascara_alta = cv2.inRange(imagem_hsv, vermelho_baixo, vermelho_alto)

# Combinar as máscaras para obter a máscara final
mascara_vermelha = cv2.bitwise_or(vermelho_mascara_baixa, vermelho_mascara_alta)

# Aplicar a máscara à imagem original 
figuras_vermelhas = cv2.bitwise_and(imagem, imagem, mask=mascara_vermelha)


