**Secure Data Hiding in Images using Stengography**  

**📌 Project Overview**  
This project is a **GUI-based Image Steganography tool** built using **Python, OpenCV, and Tkinter**. It allows users to **hide a secret message inside an image** and later **retrieve it using a password**. The message is stored within the image’s pixel values without visibly altering the image.  

**🎯 Features**  
✅ **User-Friendly GUI** – Built with Tkinter for easy interaction.  
✅ **Encryption** – Hide a secret message inside an image without noticeable changes.  
✅ **Decryption** – Retrieve the hidden message using the correct password.  
✅ **File Selection** – Users can browse and select an image for encryption or decryption.  
✅ **Security** – Only users with the correct passcode can decrypt the message.  
✅ **Error Handling** – Alerts for missing inputs, incorrect passwords, or file errors.  

## **🛠️ Technologies Used**  
- **Python** – Core programming language  
- **OpenCV** (`cv2`) – Image processing library  
- **Tkinter** – GUI development  
- **PIL (Pillow)** – Image handling for GUI  

**🚀 How It Works**  

**🔐 Encryption Process**  
1️⃣ User selects an image file.  
2️⃣ Inputs a **secret message** and **password**.  
3️⃣ The message is converted into numerical values and stored inside the image's pixel data.  
4️⃣ The modified image is saved and opened for the user.  

**🔓 Decryption Process**  
1️⃣ User selects the **modified image** for decryption.  
2️⃣ Enters the **correct password** to unlock the message.  
3️⃣ If the password matches, the hidden message is extracted and displayed.  
4️⃣ If the password is incorrect, access is denied.  

**🌟 Applications**  
🔹 **Secure Communication** – Hide confidential messages in images.  
🔹 **Digital Watermarking** – Embed hidden text into images for authenticity.  
🔹 **Data Protection** – Store sensitive information in images securely.  

**📸 Example Usage**  
1️⃣ **Encrypt an Image:**  
   - Choose an image file.  
   - Enter a secret message and a password.  
   - Click "Encrypt Image" to hide the message.  

2️⃣ **Decrypt an Image:**  
   - Select the modified image.  
   - Enter the correct password.  
   - Click "Decrypt Image" to reveal the message.

**📝 Future Enhancements**  
🔹 Add support for larger messages using advanced encoding techniques.  
🔹 Implement a **Drag-and-Drop** feature for file selection.  
🔹 Improve security using encryption before embedding the message.  
🔹 Develop a mobile or web-based version for accessibility.  

**💡 Conclusion**  
This **Image Steganography** tool provides a simple yet powerful way to **hide and retrieve messages** inside images securely. With a friendly GUI and strong encryption logic, it ensures secure data hiding without affecting image quality.  
