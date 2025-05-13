import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega os dados
train_df = pd.read_csv("sign_mnist_train.csv")
test_df = pd.read_csv("sign_mnist_test.csv")

X_train = train_df.drop("label", axis=1).values
y_train = train_df["label"].values

X_test = test_df.drop("label", axis=1).values
y_test = test_df["label"].values

# Normalização
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Criação e treinamento do modelo
mlp = MLPClassifier(hidden_layer_sizes=(100,), max_iter=300, random_state=42)
mlp.fit(X_train_scaled, y_train)

# Teste
y_pred = mlp.predict(X_test_scaled)
print("Acurácia:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Matriz de confusão
conf_mat = confusion_matrix(y_test, y_pred)

# Mapeamento de índices para letras (sem J e Z)
label_map = {i: chr(i + 65) for i in range(26)}
del label_map[9]  # Remove J
del label_map[25] # Remove Z
labels = list(label_map.values())

# Plotar matriz de confusão
plt.figure(figsize=(12, 10))
sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues',
            xticklabels=labels, yticklabels=labels)
plt.xlabel("Predito")
plt.ylabel("Verdadeiro")
plt.title("Matriz de Confusão - MLP Sign Language")
plt.show()

# Função para pré-processar a imagem da webcam
def preprocess_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (28, 28))
    flattened = resized.flatten().reshape(1, -1)
    return scaler.transform(flattened)

# Inicializa webcam
cap = cv2.VideoCapture(0)
print("Pressione 'q' para sair")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame,1)
    # Define uma região de interesse (ROI) onde a mão deve ser posicionada
    x, y, w, h = 100, 100, 250, 250
    roi = frame[y:y+h, x:x+w]

    # Processa e faz a predição
    processed = preprocess_frame(roi)
    prediction = mlp.predict(processed)[0]

    letra = label_map.get(prediction, '?')

    # Desenha retângulo e mostra a letra predita
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.putText(frame, f"Letra: {letra}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Reconhecimento de Sinais", frame)

    # Sair com a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
