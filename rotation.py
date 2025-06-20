# ---------------------------------------------------------
#   Name : Madhunicka M.
#   Reg No: EG/2020/4051
#   Assignment 1
#   Q3
# ---------------------------------------------------------
#required libraries
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import os

output_dir = os.path.join("result", "Q3")
os.makedirs(output_dir, exist_ok=True)

# Load the image
image = cv2.imread('image/input1.png')
if image is None:
    print("Error: Image not found.")
    exit()

# Image dimensions
rows, cols = image.shape[:2]

# Rotate by 45 degrees clockwise
matrix_45 = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
rotated_45 = cv2.warpAffine(image, matrix_45, (cols, rows))

# Rotate by 90 degrees clockwise
matrix_90 = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
rotated_90 = cv2.warpAffine(image, matrix_90, (cols, rows))

# Save images
cv2.imwrite(os.path.join(output_dir, "original.png"), image)
cv2.imwrite(os.path.join(output_dir, "rotated_45.png"), rotated_45)
cv2.imwrite(os.path.join(output_dir, "rotated_90.png"), rotated_90)

# Convert OpenCV image to Tk-compatible format
def to_tk(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return ImageTk.PhotoImage(Image.fromarray(img_rgb))

# Tkinter root setup
root = tk.Tk()
root.withdraw()

images = [("Original Image", image), ("Rotated 45°", rotated_45), ("Rotated 90°", rotated_90)]
open_windows = []

# Create a Toplevel window for each image
for title, img in images:
    h, w = img.shape[:2]
    win = tk.Toplevel()
    win.title(title)
    win.configure(bg="black")
    win.geometry(f"{w}x{h+40}")

    label_title = tk.Label(win, text=title, bg="black", fg="white", font=("Arial", 12, "bold"))
    label_title.pack()

    tk_img = to_tk(img)
    label_img = tk.Label(win, image=tk_img, bg="black")
    label_img.image = tk_img
    label_img.pack()

    open_windows.append(win)

    def on_close(win=win):
        open_windows.remove(win)
        win.destroy()
        if not open_windows:
            root.quit()

    win.protocol("WM_DELETE_WINDOW", on_close)

# Run GUI
root.mainloop()
