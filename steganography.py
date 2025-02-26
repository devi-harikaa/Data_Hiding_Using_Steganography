from stegano import lsb
import webbrowser
import os

# Function to hide a secret message in an image
def hide_message(input_image, output_image, secret_message):
    lsb.hide(input_image, secret_message).save(output_image)
    print(f"✅ Secret message embedded successfully in: {output_image}")
    
    # Open the output image in a new tab
    webbrowser.open(output_image)

# Function to reveal the hidden message and display it in a browser tab
def reveal_message(stego_image):
    hidden_message = lsb.reveal(stego_image)
    
    if hidden_message:
        output_text_file = "message.html"
        
        # ✅ FIX: Use UTF-8 encoding to avoid Unicode errors
        with open(output_text_file, "w", encoding="utf-8") as file:
            file.write(f"<html><body><h2>🔓 Hidden Message</h2><p>{hidden_message}</p></body></html>")
        
        print(f"🔓 Hidden message extracted and displayed in a new tab.")
        
        # Open the text file in a new browser tab
        webbrowser.open(f"file://{os.path.abspath(output_text_file)}")
    else:
        print("⚠ No hidden message found in the image!")

# User Input
choice = input("Do you want to (1) Hide a message or (2) Reveal a message? Enter 1 or 2: ")

if choice == "1":
    input_image = input("Enter the name of the input image (e.g., input.png): ")
    output_image = "stego_image.png"
    secret_message = input("Enter your secret message: ")

    hide_message(input_image, output_image, secret_message)

elif choice == "2":
    stego_image = input("Enter the name of the stego image (e.g., stego_image.png): ")
    reveal_message(stego_image)

else:
    print("⚠ Invalid choice. Please enter 1 or 2.")
