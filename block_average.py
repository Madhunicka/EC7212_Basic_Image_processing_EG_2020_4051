# ---------------------------------------------------------
#   Name : Madhunicka M.
#   Reg No: EG/2020/4051
#   Assignment 1
#   Q4
# ---------------------------------------------------------
# required libraries
import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
import os

# Output folder
output_dir = os.path.join("result", "Q4")
os.makedirs(output_dir, exist_ok=True)

# Load the image
image = cv2.imread('image/input1.png', cv2.IMREAD_COLOR)
if image is None:
    print("Error: Image not found.")
    exit()

# Block sizes to process
block_sizes = [3, 5, 7]

def process_image(image, block_size):
    processed_image = np.copy(image)
    # Ensure block size is odd
    for y in range(0, image.shape[0], block_size):
        # Ensure we don't go out of bounds
        for x in range(0, image.shape[1], block_size):
            # Calculate the region of interest (ROI)
            roi = image[y:y+block_size, x:x+block_size]
            # If the ROI is smaller than block_size, skip it
            mean_color = np.mean(roi, axis=(0, 1))
            processed_image[y:y+block_size, x:x+block_size] = mean_color
    return processed_image.astype(np.uint8)

# Processed images list
processed_images = [process_image(image, size) for size in block_sizes]

# Save all images
cv2.imwrite(os.path.join(output_dir, "original.png"), image)
for size, proc_img in zip(block_sizes, processed_images):
    cv2.imwrite(os.path.join(output_dir, f"processed_{size}x{size}.png"), proc_img)

# Convert OpenCV image to Tkinter-compatible format
def to_tk(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return ImageTk.PhotoImage(Image.fromarray(img_rgb))

# Tkinter setup
root = tk.Tk()
root.withdraw()

titles = ["Original Image"] + [f"Processed {size}x{size}" for size in block_sizes]
images = [image] + processed_images
open_windows = []

for title, img in zip(titles, images):
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

root.mainloop()
