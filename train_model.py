from ultralytics import YOLO

def train():
    # Load a pre-trained model (YOLOv8n is 'nano' - fastest; use 'yolov8m.pt' for better accuracy)
    model = YOLO('yolov8n.pt') 

    # Train the model
    results = model.train(
        data='data.yaml',  # Path to your config
        epochs=50,         # 50-100 epochs is usually good for this size
        imgsz=640,         # Image size (standard for YOLO)
        batch=16,          # Adjust based on your GPU memory
        name='plant_disease_model'
    )

if __name__ == '__main__':
    train()