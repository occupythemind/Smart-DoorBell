#! python3

import cv2
import numpy as np
from test_sound import play_bell_non_blocking
import settings

# Incase of env switch from PC to raspberry pi, where `tflite_runtime`
# will be used.
try:
    from tflite_runtime.interpreter import Interpreter
except ImportError:
    from tensorflow.lite.python.interpreter import Interpreter


# 1. Load the Model
interpreter = Interpreter(model_path=settings.MODEL_PATH)
interpreter.allocate_tensors()

# Get details for input/output
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]

# 2. Start Webcam
cap = cv2.VideoCapture(0)

print("Starting Smart Bell Test... (Press 'q' to quit)")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    # 3. Prepare Image (Sensing/Process)
    # The model expects a specific size (300x300)
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image_resized = cv2.resize(image_rgb, (width, height))
    input_data = np.expand_dims(image_resized, axis=0)

    # 4. Run Inference (Think)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    # Get results: classes (what it is) and scores (how sure it is)
    classes = interpreter.get_tensor(output_details[1]['index'])[0]
    scores = interpreter.get_tensor(output_details[2]['index'])[0]

    # Class 0 is 'Person' in the COCO dataset
    for i in range(len(scores)):
        if classes[i] == 0 and scores[i] > 0.60:
            print(f"PERSON DETECTED! Confidence: {scores[i]*100:.2f}%")
            # This is where we will eventually trigger the Bell and Telegram alert

            # NOTE: On raspberry, we won't be using this function, but would be sending
            # signals to the passive buzzer or bluetooth MP.
            
            # Meant to run on a seperate thread to avoid blocking
            play_bell_non_blocking(settings.SOUND_FILE) 

            if settings.ENV == 'pc':
                # This will enable the frame on PC
                cv2.putText(frame, "PERSON DETECTED", (50, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    if settings.ENV == 'pc':
        # Show the video feed
        cv2.imshow('Smart Bell Internal View', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()