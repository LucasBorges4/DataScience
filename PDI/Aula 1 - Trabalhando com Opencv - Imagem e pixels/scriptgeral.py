import cv2
import numpy as np
import matplotlib.pyplot as plt

# Variáveis globais para armazenar os pontos do corte
points = []

def show_image(image):
    cv2.imshow("Imagem", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_gray_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    show_image(gray)

def show_subplots(image):
    b, g, r = cv2.split(image)
    fig, axes = plt.subplots(1, 4, figsize=(12, 4))
    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0].set_title("Original")
    axes[1].imshow(b, cmap='gray')
    axes[1].set_title("Canal Azul")
    axes[2].imshow(g, cmap='gray')
    axes[2].set_title("Canal Verde")
    axes[3].imshow(r, cmap='gray')
    axes[3].set_title("Canal Vermelho")
    for ax in axes:
        ax.axis("off")
    plt.show()

def rotate_image(image):
    rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    show_image(rotated)

def resize_image(image):
    height, width = image.shape[:2]
    resized = cv2.resize(image, (int(width * 0.7), int(height * 0.7)))
    show_image(resized)

def mouse_callback(event, x, y, flags, param):
    global points, image
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        if len(points) == 2:
            x1, y1 = points[0]
            x2, y2 = points[1]
            cropped = image[min(y1, y2):max(y1, y2), min(x1, x2):max(x1, x2)]
            show_image(cropped)
            points = []

if __name__ == "__main__":
    image = cv2.imread("imagem.jpg")  # Substitua pelo caminho correto da imagem
    if image is None:
        print("Erro ao carregar a imagem.")
    else:
        while True:
            print("\nEscolha uma opção:")
            print("1 - Mostrar Imagem")
            print("2 - Mostrar em Tons de Cinza")
            print("3 - Mostrar Subplots (Original e Canais BGR)")
            print("4 - Rotacionar 90 Graus")
            print("5 - Redimensionar para 70%")
            print("6 - Selecionar Região para Recorte")
            print("7 - Sair")
            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                show_image(image)
            elif opcao == "2":
                show_gray_image(image)
            elif opcao == "3":
                show_subplots(image)
            elif opcao == "4":
                rotate_image(image)
            elif opcao == "5":
                resize_image(image)
            elif opcao == "6":
                cv2.imshow("Selecione dois pontos", image)
                cv2.setMouseCallback("Selecione dois pontos", mouse_callback)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif opcao == "7":
                break
            else:
                print("Opção inválida!")
