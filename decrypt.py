import cv2
def decrypt_image(image_path, password, original_message_length, original_password):
    img = cv2.imread(image_path)  # Load image

    if img is None:
        print("Error: Image not found.")
        return

    # Create a dictionary to map numbers back to characters
    num_to_char = {i: chr(i) for i in range(255)}

    entered_pass = input("Enter passcode for Decryption: ")

    if entered_pass != original_password:
        print("YOU ARE NOT AUTHORIZED")
        return

    message = ""
    n, m, z = 0, 0, 0  # Pixel coordinates

    for _ in range(original_message_length):
        message += num_to_char[img[n, m, z]]  # Retrieve character from pixel value
        n += 1
        m += 1
        z = (z + 1) % 3  # Switch between RGB channels

    print("Decrypted message:", message)

# Get user input and decrypt
image_path = "encryptedImage.jpg"  # Path of encrypted image
decrypt_image(image_path, password, len(message), password)
