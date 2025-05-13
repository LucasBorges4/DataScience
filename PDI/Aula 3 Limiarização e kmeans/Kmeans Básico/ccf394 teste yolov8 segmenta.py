from ultralytics import YOLO
import cv2
model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8m-seg.pt")  # load a pretrained model (recommended for training)
results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image

for result in results:
        boxes = result.boxes  # Boxes object for bbox outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Class probabilities for classification outputs

        res_plotted = results[0].plot()
        cv2.imshow("result", res_plotted)
        cv2.waitKey(0)
cv2.destroyAllWindows()


from ultralytics import YOLO

# Load a COCO-pretrained YOLO12n model
model = YOLO("yolo12n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLO12n model on the 'bus.jpg' image
results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
for result in results:
        boxes = result.boxes  # Boxes object for bbox outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Class probabilities for classification outputs

        res_plotted = results[0].plot()
        cv2.imshow("result", res_plotted)
        cv2.waitKey(0)
cv2.destroyAllWindows()


