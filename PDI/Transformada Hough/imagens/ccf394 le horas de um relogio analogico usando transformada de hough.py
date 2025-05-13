import cv2
import numpy as np
import math

def detectar_horario(imagem_path):
    # Carrega imagem e converte para escala de cinza
    img = cv2.imread(imagem_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    # Detecta círculos com Hough
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=100,
                               param1=100, param2=30, minRadius=100, maxRadius=0)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        x, y, r = circles[0][0]
        centro = (x, y)

        # Desenha o círculo detectado
        cv2.circle(img, centro, r, (0, 255, 0), 2)
        cv2.circle(img, centro, 2, (0, 0, 255), 3)

        # Máscara para a área do relógio
        mask = np.zeros_like(gray)
        cv2.circle(mask, centro, r, 255, thickness=-1)
        roi = cv2.bitwise_and(gray, gray, mask=mask)

        # Detecta linhas com HoughLinesP
        edges = cv2.Canny(roi, 50, 150, apertureSize=3)
        cv2.imshow("filtrada", edges)
        cv2.waitKey(0)
        linhas = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100,
                                 minLineLength=r//2, maxLineGap=15)

        ponteiros = []
        if linhas is not None:
            for linha in linhas:
                x1, y1, x2, y2 = linha[0]

                # Desenha todas as linhas detectadas em verde claro
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 180), 1)

                # Verifica se passa próximo ao centro (é ponteiro)
                dist_centro = np.hypot(((x1+x2)//2) - x, ((y1+y2)//2) - y)
                comprimento = np.hypot(x2 - x1, y2 - y1)
                if dist_centro < r * 0.1:
                    ponteiros.append(((x1, y1), (x2, y2), comprimento))
        cv2.imshow("filtrada",img)
        cv2.waitKey(0)

        # Ordena os ponteiros: maior = minuto, menor = hora
        ponteiros = sorted(ponteiros, key=lambda p: -p[2])
        if len(ponteiros) >= 2:
            min_ptr = ponteiros[0]
            hr_ptr = ponteiros[1]

            def calcular_angulo(ponto1, ponto2):
                dx = ponto2[0] - ponto1[0]
                dy = ponto1[1] - ponto2[1]  # y invertido
                angulo = math.degrees(math.atan2(dy, dx))
                return (angulo + 360) % 360

            def ajustar_ponta(ponteiro):
                if np.hypot(ponteiro[0][0] - x, ponteiro[0][1] - y) > \
                   np.hypot(ponteiro[1][0] - x, ponteiro[1][1] - y):
                    return ponteiro[1], ponteiro[0]
                else:
                    return ponteiro[0], ponteiro[1]

            centro, ponta_min = ajustar_ponta(min_ptr)
            centro, ponta_hr = ajustar_ponta(hr_ptr)

            angulo_min = calcular_angulo(centro, ponta_min)
            angulo_hr = calcular_angulo(centro, ponta_hr)

            minutos = int(round(angulo_min / 6)) % 60
            horas = int((angulo_hr / 30)) % 12
            if minutos > 45:
                horas = (horas + 1) % 12

            print(f"Horário detectado: {horas:02d}:{minutos:02d}")

            # Desenha os dois ponteiros principais
            cv2.line(img, centro, ponta_min, (255, 0, 0), 2)   # Minuto: azul
            cv2.line(img, centro, ponta_hr, (0, 0, 255), 4)   # Hora: vermelho

        else:
            print("Não foi possível detectar dois ponteiros válidos.")
    else:
        print("Relógio não detectado.")

    # Exibe resultado final
    cv2.imshow("Resultado", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Exemplo de uso
detectar_horario("clock.png")
