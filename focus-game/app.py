import cv2
import tkinter as tk
from tkinter import messagebox
import time
import os

# Load Haar cascades for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade  = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Game variables
score = 0
high_score = 0
running = False

# Load high score from file
def load_high_score():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as f:
            return int(f.read())
    return 0

# Save high score to file
def save_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))

# Check if eyes are open using webcam
def check_focus():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    eyes_open = False

    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            roi = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi)
            if len(eyes) >= 2:
                eyes_open = True
                break

    cap.release()
    return eyes_open

# Update score every second
def update_score():
    global score, running, high_score
    if not running:
        return

    focused = check_focus()
    if focused:
        score += 1
        score_label.config(text=f"Score: {score} 🧠")
        root.after(1000, update_score)
    else:
        running = False
        messagebox.showinfo("😴 Game Over", f"You lost focus!\nFinal Score: {score}")
        if score > high_score:
            save_high_score(score)
            high_label.config(text=f"🏆 New High Score: {score}")
        else:
            high_label.config(text=f"High Score: {high_score}")

# Start the game
def start_game():
    global score, running, high_score
    score = 0
    running = True
    high_score = load_high_score()
    score_label.config(text="Score: 0 🧠")
    high_label.config(text=f"High Score: {high_score}")
    update_score()

# GUI setup
root = tk.Tk()
root.title("🎯 Focus Hero")
root.geometry("350x300")
root.resizable(False, False)

title = tk.Label(root, text="🎯 Focus Hero", font=("Arial", 24))
title.pack(pady=10)

score_label = tk.Label(root, text="Score: 0 🧠", font=("Arial", 16))
score_label.pack(pady=5)

high_label = tk.Label(root, text="High Score: 0", font=("Arial", 14))
high_label.pack(pady=5)

start_btn = tk.Button(root, text="Start Game", command=start_game, font=("Arial", 14), bg="green", fg="white")
start_btn.pack(pady=20)

emoji_label = tk.Label(root, text="😎 Stay focused to win!", font=("Arial", 16))
emoji_label.pack(pady=10)

root.mainloop()