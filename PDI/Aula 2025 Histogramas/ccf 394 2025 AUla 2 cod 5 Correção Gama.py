import cv2
import numpy as np

def calcular_gamma(img, metodo="media"):
    """ Calcula o valor ótimo de gamma baseado no método escolhido """
    img_norm = img / 255.0  # Normaliza para o intervalo [0,1]
    
    if metodo == "media":
        media = np.mean(img_norm)
        gamma = np.log(0.5) / np.log(media) if media > 0 else 1.0
    elif metodo == "percentil":
        percentil_50 = np.percentile(img_norm, 50)
        gamma = np.log(0.5) / np.log(percentil_50) if percentil_50 > 0 else 1.0
    elif metodo == "inverso_media":
        media = np.mean(img_norm)
        gamma = 1 - media if media > 0 else 1.0
    else:
        gamma = 1.0  # Valor padrão se o método não for reconhecido
    
    return gamma

def aplicar_correcao_gamma(img, gamma):
    """ Aplica a correção gama na imagem """
    lut = np.array([(i / 255.0) ** gamma * 255 for i in range(256)]).astype("uint8")
    return cv2.LUT(img, lut)

# Leitura da imagem
caminho_imagem = "tipos de calculo de correcao gama.png"  # Substitua pelo caminho correto da sua imagem
img = cv2.imread(caminho_imagem)
cv2.imshow("Cálculos de Gamma",img)
cv2.waitKey(3000)


caminho_imagem = "wiki.png"  # Substitua pelo caminho correto da sua imagem
img = cv2.imread(caminho_imagem)

# Verifica se a imagem foi carregada corretamente
if img is None:
    print("Erro ao carregar a imagem. Verifique o caminho do arquivo.")
else:
    # Converte para escala de cinza
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Calcula gamma pelos três métodos
    gamma_media = calcular_gamma(img_gray, metodo="media")
    gamma_percentil = calcular_gamma(img_gray, metodo="percentil")
    gamma_inverso_media = calcular_gamma(img_gray, metodo="inverso_media")

    print(f"Gamma (media): {gamma_media:.4f}")
    print(f"Gamma (percentil 50): {gamma_percentil:.4f}")
    print(f"Gamma (1 - media): {gamma_inverso_media:.4f}")

    # Aplica as correções
    img_corrigida_media = aplicar_correcao_gamma(img_gray, gamma_media)
    img_corrigida_percentil = aplicar_correcao_gamma(img_gray, gamma_percentil)
    img_corrigida_inverso_media = aplicar_correcao_gamma(img_gray, gamma_inverso_media)

    # Combina as imagens para exibição
    resultado = np.hstack((img_gray, img_corrigida_media, img_corrigida_percentil, img_corrigida_inverso_media))

    # Exibe as imagens
    cv2.imshow("Original                | Gama (media)      | Gama (percentil)     | Gama (1 - media)", resultado)
    
    # Salvar as imagens corrigidas
    cv2.imwrite("imagem_corrigida_media.jpg", img_corrigida_media)
    cv2.imwrite("imagem_corrigida_percentil.jpg", img_corrigida_percentil)
    cv2.imwrite("imagem_corrigida_inverso_media.jpg", img_corrigida_inverso_media)

    # Aguarda uma tecla e fecha as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()
