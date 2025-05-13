import cv2
import numpy as np

# Abrir o vídeo com chroma key (fundo verde)
video = cv2.VideoCapture("thanos.mp4")

# Abrir a webcam
webcam = cv2.VideoCapture(0)

# Verificar se os arquivos abriram corretamente
if not video.isOpened() or not webcam.isOpened():
    print("Erro ao abrir vídeo ou webcam")
    exit()

# Obter as dimensões do vídeo e a taxa de quadros
frame_width = int(webcam.get(3))
frame_height = int(webcam.get(4))
fps = int(video.get(cv2.CAP_PROP_FPS))

# Definir o codec e criar o objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, fps, (frame_width, frame_height))

while True:
    # Ler um frame do vídeo e da webcam
    ret_video, frame_video = video.read()
    ret_webcam, frame_webcam = webcam.read()

    # Se o vídeo acabar, reiniciar
    if not ret_video:
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # Se a webcam falhar, sair
    if not ret_webcam:
        break

    # Redimensionar o vídeo para o tamanho da webcam
    frame_video = cv2.resize(frame_video, (frame_width, frame_height))

    # Criar máscara para identificar o fundo verde
    lower_green = np.array([0, 100, 0], dtype=np.uint8)
    upper_green = np.array([100, 255, 100], dtype=np.uint8)
    mask = cv2.inRange(frame_video, lower_green, upper_green)

    # Substituir os pixels verdes pelo frame da webcam
    frame_video[np.where(mask != 0)] = frame_webcam[np.where(mask != 0)]

    # Escrever o frame processado no arquivo de saída
    out.write(frame_video)

    # Exibir o resultado
    cv2.imshow("Chroma Key", frame_video)

    # Pressione ESC para sair
    if cv2.waitKey(1) == 27:
        break

# Liberar recursos
video.release()
webcam.release()
out.release()
cv2.destroyAllWindows()

