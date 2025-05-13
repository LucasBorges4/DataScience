
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

# Carregar o conjunto de dados MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizar os dados para o intervalo [0, 1]
x_train = x_train / 255.0
x_test = x_test / 255.0

# Definir a arquitetura da rede neural
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Achatar as imagens 28x28 em vetores 1D
    layers.Dense(128, activation='relu'),  # Camada densa com 128 neurônios e ReLU
    layers.Dropout(0.2),  # Camada de dropout para regularização
    layers.Dense(10, activation='softmax')  # Camada de saída com 10 neurônios (um para cada dígito)
])

# Compilar o modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Treinar o modelo
model.fit(x_train, y_train, epochs=5)

# Avaliar o modelo nos dados de teste
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Loss: {test_loss}')
print(f'Accuracy: {test_acc}')

# Fazer previsões com o modelo treinado
predictions = model.predict(x_test)

# Mostrar a primeira imagem de teste e a previsão do modelo
plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.title(f'Predição: {tf.argmax(predictions[0]).numpy()}')
plt.show()

'''
Explicação do Código:
Carregar o MNIST: O código começa carregando o conjunto de dados MNIST com mnist.load_data(), que já está dividido em dados de treinamento (x_train, y_train) e de teste (x_test, y_test).

Normalização: As imagens são normalizadas para o intervalo [0, 1], dividindo os valores de pixel por 255. Isso ajuda o modelo a treinar mais rapidamente.

Modelo:

A primeira camada é uma camada Flatten, que transforma as imagens 2D de 28x28 pixels em vetores 1D.

Em seguida, temos uma camada densa (Dense) com 128 neurônios e a função de ativação ReLU.

A camada Dropout(0.2) é usada para regularização e evitar overfitting.

Finalmente, a camada de saída tem 10 neurônios, representando os 10 dígitos (0-9), com a função de ativação softmax.

Compilação do Modelo: Usamos o otimizador Adam, a função de perda sparse_categorical_crossentropy (adequada para classificação multiclasse) e a métrica de precisão.

Treinamento: O modelo é treinado por 5 épocas.

Avaliação: O modelo é avaliado usando os dados de teste.

Previsões: O modelo faz previsões sobre o conjunto de teste e, finalmente, a primeira imagem é exibida com a previsão do modelo.
'''
