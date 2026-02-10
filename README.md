# AgriVision-YOLO: Multi-Crop Disease Detection 🌱🔍

**AgriVision-YOLO** is a computer vision system designed to detect and diagnose plant diseases from leaf images in real-time. Built with **YOLOv8** for state-of-the-art object detection and **FastAPI** for the backend, this project identifies over 30 different classes of plant diseases across crops like Banana, Chilli, Rice, and Wheat.

## 🚀 Features
* **Real-time Detection:** Instantly identifies diseases and healthy conditions.
* **Visual Feedback:** Returns images with bounding boxes and confidence scores drawn around detected diseases.
* **30+ Classes:** Capable of detecting complex diseases like *Chilli Leaf Curl*, *Banana Sigatoka*, and *Rice Blast*.
* **Lightweight Backend:** Powered by FastAPI for high performance and easy integration.

## 📂 Dataset
Due to file size limits, the dataset is not included in this repository.

**Source:** [Multi-Crop Leaf Disease Dataset (Mendeley Data)](https://data.mendeley.com/datasets/6243z8r6t6/1)  
**Size:** ~23,000 Images  

### How to use the dataset:
1.  Download the dataset from the link above.
2.  Extract the images.
3.  Update the `data.yaml` file in this project to point to your local dataset path if you intend to retrain the model.

## 🛠️ Tech Stack
* **Model:** YOLOv8 (Ultralytics)
* **Backend:** FastAPI, Uvicorn
* **Image Processing:** OpenCV, PIL (Pillow)
* **Language:** Python 3.9+

## ⚙️ Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/AgriVision-YOLO.git](https://github.com/your-username/AgriVision-YOLO.git)
    cd AgriVision-YOLO
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Download the Weights:**
    * If you have trained your own model, place your `best.pt` file in the root directory.
    * *(Optional: If you hosted your model release elsewhere, add a link here).*

## 🏃‍♂️ How to Run

1.  **Start the Server:**
    Run the following command in your terminal:
    ```bash
    python main.py
    ```
    You should see: `Uvicorn running on http://0.0.0.0:8000`

2.  **Test the API:**
    * Open your browser and go to: [http://localhost:8000/docs](http://localhost:8000/docs)
    * Click on the **POST /detect** endpoint.
    * Click **Try it out** -> **Upload** an image of a plant leaf -> **Execute**.
    * You will receive the image back with the disease detected and highlighted.

## 📊 Model Performance
* **Model Architecture:** YOLOv8n (Nano)
* **mAP50:** ~75% (Initial prototype)
* **Strongest Detections:** Banana Healthy, Groundnut Rust, Radish Flea Beetle (>95% accuracy).

## 👤 Author
**Sarath Kumar** 

