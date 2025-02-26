import cv2
import pyautogui
import numpy as np
import os
import winsound
import threading
import tkinter as tk
from tkinter import Label, Button, PhotoImage
from twilio.rest import Client
from PIL import Image, ImageTk

# Absolute paths for YOLO files
WEIGHTS_PATH = r"C:\Users\harsh\OneDrive\Desktop\ai\models\yolov3.weights"
CFG_PATH = r"C:\Users\harsh\OneDrive\Desktop\ai\models\yolov3.cfg"
NAMES_PATH = r"C:\Users\harsh\OneDrive\Desktop\ai\models\coco.names"

# Load YOLO model
yolo_net = cv2.dnn.readNet(WEIGHTS_PATH, CFG_PATH)
layer_names = yolo_net.getLayerNames()
out_layers = [layer_names[i - 1] for i in yolo_net.getUnconnectedOutLayers()]
classes = open(NAMES_PATH).read().strip().split("\n")

# Twilio Credentials
TWILIO_SID = "YOUR TWILIO ID"
TWILIO_AUTH = "TWILIO AUTH"
TO_WHATSAPP = "whatsapp:+91XXXXXXXXXX"
FROM_WHATSAPP = "whatsapp:+14155238886"

# Tkinter UI Setup
root = tk.Tk()
root.title("🚨 AI-Powered Security System 🚨")
root.geometry("1200x800")
root.configure(bg="black")



# UI Elements
status_label = Label(root, text="🚨 Monitoring System Active 🚨", font=("Arial", 18), fg="red", bg="black")
status_label.pack()

video_label = Label(root, bg="black")
video_label.pack()

def play_alarm():
    for _ in range(3):
        winsound.Beep(1500, 800)

def detect_camera(frame):
    height, width = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), swapRB=True, crop=False)
    yolo_net.setInput(blob)
    outputs = yolo_net.forward(out_layers)
    
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.3 and classes[class_id] in ["cell phone", "camera"]:
                return True
    return False

def capture_screenshot():
    screenshot_path = r"C:\Users\harsh\OneDrive\Desktop\ai\screenshot.png"
    pyautogui.screenshot().save(screenshot_path)
    return screenshot_path

def capture_intruder():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    intruder_path = r"C:\Users\harsh\OneDrive\Desktop\ai\intruder.jpg"
    if ret:
        cv2.imwrite(intruder_path, frame)
    cap.release()
    return intruder_path

def send_whatsapp_alert():
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH)
        client.messages.create(
            from_=FROM_WHATSAPP,
            body="🚨 Unauthorized camera detected! Please check.",
            to=TO_WHATSAPP
        )
        status_label.config(text="✅ WhatsApp alert sent!", fg="green")
    except Exception as e:
        status_label.config(text=f"❌ Failed to send alert: {e}", fg="red")

def monitor_security():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            status_label.config(text="❌ Camera error!", fg="red")
            break
        
        if detect_camera(frame):
            status_label.config(text="🚨 Security Alert! Unauthorized recording device detected! 📸⚠️ Immediate action required!", fg="yellow")
            play_alarm()
            capture_screenshot()
            capture_intruder()
            send_whatsapp_alert()
            break
        
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)
        root.update()
    
    cap.release()
    cv2.destroyAllWindows()

def start_monitoring():
    threading.Thread(target=monitor_security).start()

def stop_monitoring():
    status_label.config(text="Monitoring Stopped", fg="white")
    root.quit()

# Buttons
start_btn = Button(root, text="Start Monitoring", command=start_monitoring, font=("Arial", 20), bg="green", fg="white")
start_btn.pack()
stop_btn = Button(root, text="Stop Monitoring", command=stop_monitoring, font=("Arial", 20), bg="red", fg="white")
stop_btn.pack()

root.mainloop()





