import cv2
import os

def encrypt_image(image_path, message, password, output_path="encryptedImage.jpg"):
    img = cv2.imread(image_path)  # Load image

    if img is None:
        print("Error: Image not found.")
        return

    # Create a dictionary to map characters to numbers
    char_to_num = {chr(i): i for i in range(255)}

    n, m, z = 0, 0, 0  # Pixel coordinates

    for char in message:
        img[n, m, z] = char_to_num[char]  # Store message in pixel values
        n += 1
        m += 1
        z = (z + 1) % 3  # Switch between RGB channels

    cv2.imwrite(output_path, img)  # Save the modified image
    os.system(f"start {output_path}")  # Open the image
    print("Encryption complete. Image saved as:", output_path)

# Get user input and encrypt
image_path = r"V:\stnego\pic.png"  # Replace with correct path
message = input("Enter secret message: ")
password = input("Enter a passcode: ")
encrypt_image(image_path, message, password)
