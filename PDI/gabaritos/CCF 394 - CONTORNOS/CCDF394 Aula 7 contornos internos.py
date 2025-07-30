import cv2

def on_trackbar_change(position):
    # Atualiza o índice do contorno selecionado
    global selected_contour
    selected_contour = position

# Leitura da imagem
image = cv2.imread("figurasdiversas.png")

# Encontra os contornos na imagem
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Inicializa o índice do contorno selecionado
selected_contour = 0
print(len(contours))
# Cria a janela de exibição
cv2.namedWindow("Contornos")

# Cria a trackbar para selecionar o contorno
cv2.createTrackbar("Contorno", "Contornos", selected_contour, len(contours) - 1, on_trackbar_change)

while True:
    # Cria uma cópia da imagem original
    output = image.copy()

    # Desenha o contorno selecionado na imagem de saída
    cv2.drawContours(output, [contours[selected_contour]], -1, (0, 0, 222), 2)

    # Exibe a imagem de saída
    cv2.imshow("Contornos", output)

    # Verifica se a tecla 'q' foi pressionada para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera os recursos e fecha as janelas
cv2.destroyAllWindows()
