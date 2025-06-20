# ---------------------------------------------------------
#   Name : Madhunicka M.
#   Reg No: EG/2020/4051
#   Assignment 1
#   Q1
# ---------------------------------------------------------
# required libraries
import cv2
import tkinter as tk
from tkinter import Scale, HORIZONTAL
from PIL import Image, ImageTk
import os

# Load image in grayscale
image = cv2.imread('image/input1.png', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Image not found.")
    exit()

# Create output directory
output_dir = "result/Q1"
os.makedirs(output_dir, exist_ok=True)

# Function to update image based on trackbar value
def update(val):
    power = int(val)
    levels = 2 ** power
    step = 256 // levels
    quantized = (image // step) * step

    # Convert to display format
    img_pil = Image.fromarray(quantized)
    img_tk = ImageTk.PhotoImage(image=img_pil)

    label.config(image=img_tk)
    label.image = img_tk
    info_label.config(text=f"Power: {power}, Levels: {levels}")

    # Save the quantized image
    filename = f"quantized_power_{power}.png"
    cv2.imwrite(os.path.join(output_dir, filename), quantized)

# Setup Tkinter window
root = tk.Tk()
root.title("Custom Intensity Quantization")
root.configure(bg="black")

# Initial setup
init_power = 3
init_levels = 2 ** init_power
step = 256 // init_levels
quantized_init = (image // step) * step
img_init = ImageTk.PhotoImage(image=Image.fromarray(quantized_init))

# Label to show image
label = tk.Label(root, image=img_init, bg="black")
label.pack()

# Label to show information
info_label = tk.Label(root, text=f"Power: {init_power}, Levels: {2**init_power}",
                      fg="white", bg="black", font=("Arial", 12))
info_label.pack(pady=5)

# Slider for intensity adjustment
slider = Scale(root, from_=1, to=8, orient=HORIZONTAL, command=update, length=400,
               fg='white', bg='black', troughcolor='gray', highlightthickness=0)
slider.set(init_power)
slider.pack()

# Save initial image
cv2.imwrite(os.path.join(output_dir, f"quantized_power_{init_power}.png"), quantized_init)

root.mainloop()

