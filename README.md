# 🔔 SMART-DOORBELL
Smart DoorBell is a smart vision-based system that detects whether someone is at your door.
When a person is detected, the system triggers an alarm (doorbell).

## 📐👷🏻‍♀️ Architectural Design
![Smart Doorbell Setup](design/architecture-design.drawio.png)

## 🚀 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/occupythemind/Smart-DoorBell.git
cd Smart-DoorBell
```

### 2️⃣ Create & activate a virtual environment
```bash
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
```

### 3️⃣ Install dependencies

🖥️ On Personal Computer (PC) — Prototype
```bash
pip install opencv-python tensorflow numpy
```

🍓 On Raspberry Pi
```bash
pip install opencv-python tflite-runtime numpy
```

### 4️⃣ Download the TensorFlow Lite model
```bash
wget http://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip
unzip coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip
```

## ▶️ Run the Project
```bash
chmod +x test_bell.py
./test_bell.py
```

## 📁 Notes
- The PC version uses TensorFlow for prototyping.
- The Raspberry Pi version uses tflite-runtime for better performance and lower resource usage.
- Make sure your camera is properly connected and accessible.
