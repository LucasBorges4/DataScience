from ultralytics import YOLO
import cv2
model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8m-seg.pt")  # load a pretrained model (recommended for training)
# Inicializar a webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro ao acessar a webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)  # predict on an image

    for result in results:
        boxes = result.boxes  # Boxes object for bbox outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Class probabilities for classification outputs

        res_plotted = results[0].plot()
        cv2.imshow("result", res_plotted)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):q
            break
        else:
        # Break the loop if the end of the video is reached
          break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()

