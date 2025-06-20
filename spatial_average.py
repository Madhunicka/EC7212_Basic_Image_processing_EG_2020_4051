# ---------------------------------------------------------
#   Name : Madhunicka M.
#   Reg No: EG/2020/4051
#   Assignment 1
#   Q2
# ---------------------------------------------------------
# required libraries
import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
import os

# Initialize Tkinter root 
root = tk.Tk()
root.withdraw() 

output_dir = os.path.join("result", "Q2")
os.makedirs(output_dir, exist_ok=True)

# Load the image
image = cv2.imread('image/input1.png')
if image is None:
    print("Error: Image not found.")
    exit()

# Apply spatial averaging
avg_3x3 = cv2.blur(image, (3, 3))
avg_10x10 = cv2.blur(image, (10, 10))
avg_20x20 = cv2.blur(image, (20, 20))

# Save the results
cv2.imwrite(os.path.join(output_dir, "average_3x3.png"), avg_3x3)
cv2.imwrite(os.path.join(output_dir, "average_10x10.png"), avg_10x10)
cv2.imwrite(os.path.join(output_dir, "average_20x20.png"), avg_20x20)

# Convert OpenCV to PIL for display
def convert_to_tk(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return ImageTk.PhotoImage(Image.fromarray(img_rgb))

# Titles and images
titles = ["Original", "3x3 Avg", "10x10 Avg", "20x20 Avg"]
images = [image, avg_3x3, avg_10x10, avg_20x20]

open_windows = []  # Track all opened windows

for i, img in enumerate(images):
    img_tk = convert_to_tk(img)
    h, w = img.shape[:2]

    win = tk.Toplevel()
    win.title(titles[i])
    win.configure(bg="black")
    win.geometry(f"{w}x{h+40}")

    label_title = tk.Label(win, text=titles[i], bg="black", fg="white", font=("Arial", 12, "bold"))
    label_title.pack()

    label_img = tk.Label(win, image=img_tk, bg="black")
    label_img.image = img_tk
    label_img.pack()

    open_windows.append(win)

    # Exit if all windows are closed
    def on_close(win=win):
        open_windows.remove(win)
        win.destroy()
        if not open_windows:
            root.quit()

    win.protocol("WM_DELETE_WINDOW", on_close)


root.mainloop()
