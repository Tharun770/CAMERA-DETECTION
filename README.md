# CAMERA-DETECTION
<h3>🚨AI-Powered Unauthorized Camera Detection System 🚨</h3>

<h1>Overview</h1>

<p>1.This AI-powered security system detects unauthorized cameras or mobile phones attempting to capture sensitive data. If detected, it:Plays an alarm 🚨<br>

2.Captures a screenshot of the current screen 📸<br>

3.Captures an intruder's image using the webcam 👀<br>

4.Sends a WhatsApp alert with a warning message 📲<br>

4.Provides a real-time video feed with a modern, colorful Tkinter UI 🎨<br>


<h2>Features</h2>

✅ Real-time Object Detection using YOLOv3 for identifying cameras/phones.<br>✅ Instant Alerts via WhatsApp using Twilio API.<br>✅ Loud Alarm using system beeps for immediate response.<br>✅ User-Friendly Tkinter Interface with dynamic elements and live feed.<br>✅ Multithreading for a smooth UI experience.

<h2>Technologies Used<h2></h2>

Python 🐍

OpenCV (Image Processing & Webcam Integration)

YOLOv3 (Object Detection)

Twilio API (WhatsApp Alert Notifications)

Tkinter (Graphical User Interface)

PyAutoGUI (Automated Screenshot Capture)

PIL (Pillow) (Image Handling for Tkinter UI)

Winsound (Alarm Sound for Windows)

Threading (Smooth UI & Background Processing)

<h1>Installation</h1>

Step 1: Clone the Repository

git clone https://github.com/Tharun770/CAMERA-DETECTION/tree/master/ai
cd camera-detection-system

Step 2: Install Dependencies

👉pip install opencv-python numpy twilio pyautogui pillow winsound

Step 3: Download YOLOv3 Model Files

👉Place the following files inside models/ directory:

yolov3.weights

yolov3.cfg

coco.names

👉You can download them from:

YOLOv3 Weights

YOLOv3 Config

COCO Names

Step 4: Configure Twilio API

👉<h3>Create a Twilio Account and set up a WhatsApp sandbox. Replace the following in the script:</h3>

TWILIO_SID = "your_twilio_sid"<br>
TWILIO_AUTH = "your_twilio_auth_token"<br>
TO_WHATSAPP = "whatsapp:+91XXXXXXXXXX"<br>
FROM_WHATSAPP = "whatsapp:+14155238886"<br>

Step 5: Run the Application

python app.py

<h1>Usage</h1>

1.Start Monitoring by clicking the Start button.

2.The system continuously scans for unauthorized cameras.

3.If a phone or camera is detected, the system:

4.Plays an alarm

5.Takes a screenshot of the screen

6.Captures an image of the intruder

7.Sends a WhatsApp alert

8.Press Stop to exit the application.


<h1>Future Enhancements</h1>

🔹 Facial Recognition for authorized personnel to reduce false alarms.<br>🔹 Multi-Camera Support to monitor different angles.<br>🔹 Cloud Integration to store detection logs and images remotely.

📌 Contributors: THARUN KUMAR B<BR> 📌 Contact:tharunkumarb98676@gmail.com.com

🚀 Stay Secure, Stay Alert!

