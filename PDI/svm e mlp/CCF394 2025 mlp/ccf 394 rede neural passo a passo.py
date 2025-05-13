import numpy as np
import matplotlib.pyplot as plt

# Dados de entrada e saída
X = np.array([2, 5, 3])
y = np.array(850)

# Inicialização dos pesos
np.random.seed(42)
W=[50 ,50 ,50]

# Taxa de aprendizado
learning_rate = 0.0001


# Número de iterações (épocas)
num_epochs = 3000

# Lista para armazenar os erros durante o treinamento
errors = []

# Treinamento da rede neural
for epoch in range(num_epochs):
    # Forward pass
    output = X.dot(W)
    #print(output)
    
    # Cálculo do erro
    error =  y.T - output  # Transpor y para manter o formato correto
    #print(error)
   
    errors.append(error)
    
    # Backpropagation para ajustar os pesos
    grad_W = learning_rate *X*(error)
    #grad_W=np.reshape(3,1)
    print(" Saida %d, Erro: %d, Grad_w: %s" %(output,error,grad_W))
    
    # Atualização dos pesos
    W += grad_W
    print(W)
    if error<0.1:
         break
# Print dos pesos finais
print("Pesos finais:")
print(W)
print("Conta com o peso calculado %d" % np.dot(W, X))
# Plotagem dos erros durante o treinamento
plt.plot(errors)
plt.title('Erro durante o treinamento')
plt.xlabel('Época')
plt.ylabel('Erro')
plt.show()


