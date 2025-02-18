import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Encryption Function
def encrypt_image():
    file_path = filedialog.askopenfilename(title="Select an Image")
    if not file_path:
        return

    message = msg_entry.get()
    password = pass_entry.get()

    if not message or not password:
        messagebox.showerror("Error", "Message and password cannot be empty!")
        return

    img = cv2.imread(file_path)

    if img is None:
        messagebox.showerror("Error", "Failed to open image!")
        return

    char_to_num = {chr(i): i for i in range(255)}

    n, m, z = 0, 0, 0

    for char in message:
        img[n, m, z] = char_to_num[char]
        n += 1
        m += 1
        z = (z + 1) % 3

    output_path = "encryptedImage.jpg"
    cv2.imwrite(output_path, img)
    os.system(f"start {output_path}")

    global stored_password
    stored_password = password
    global message_length
    message_length = len(message)

    messagebox.showinfo("Success", f"Message encrypted and saved as {output_path}")

# Decryption Function
def decrypt_image():
    file_path = filedialog.askopenfilename(title="Select Encrypted Image")
    if not file_path:
        return

    entered_pass = pass_entry.get()

    if entered_pass != stored_password:
        messagebox.showerror("Error", "Incorrect password!")
        return

    img = cv2.imread(file_path)

    if img is None:
        messagebox.showerror("Error", "Failed to open image!")
        return

    num_to_char = {i: chr(i) for i in range(255)}

    message = ""
    n, m, z = 0, 0, 0

    for _ in range(message_length):
        message += num_to_char[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3

    decrypted_msg.set(message)

# GUI Setup
root = tk.Tk()
root.title("Image Steganography")
root.geometry("500x400")

stored_password = ""
message_length = 0
decrypted_msg = tk.StringVar()

# UI Elements
tk.Label(root, text="Secret Message:").pack(pady=5)
msg_entry = tk.Entry(root, width=50)
msg_entry.pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
pass_entry = tk.Entry(root, width=50, show="*")
pass_entry.pack(pady=5)

tk.Button(root, text="Encrypt Image", command=encrypt_image).pack(pady=10)
tk.Button(root, text="Decrypt Image", command=decrypt_image).pack(pady=10)

tk.Label(root, text="Decrypted Message:").pack(pady=5)
tk.Entry(root, textvariable=decrypted_msg, width=50, state="readonly").pack(pady=5)

# Run GUI
root.mainloop()
