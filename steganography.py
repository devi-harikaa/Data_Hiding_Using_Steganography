from stegano import lsb
import webbrowser
pip install -r requirements.txt
# Function to encode a message into an image
def hide_message(input_image, output_image, secret_message):
    lsb.hide(input_image, secret_message).save(output_image)
    print(f"✅ Secret message embedded successfully in: {output_image}")
    
    # Open the output image in a new tab
    webbrowser.open(output_image)

# Function to extract a hidden message and save it to a text file
def reveal_message(stego_image, output_text_file):
    hidden_message = lsb.reveal(stego_image)
    
    if hidden_message:
        with open(output_text_file, "w") as file:
            file.write(hidden_message)
        print(f"🔓 Hidden message extracted and saved to: {output_text_file}")

        # Open the text file
        webbrowser.open(output_text_file)
    else:
        print("⚠ No hidden message found in the image!")

# User Input
choice = input("Do you want to (1) Hide a message or (2) Reveal a message? Enter 1 or 2: ")

if choice == "1":
    input_image = input("Enter the name of the input image (e.g., input.png): ")
    output_image = "stego_image.png"
    secret_message = """In the vast world of data, secrets are hidden where no one looks. 
    Within these pixels lies a story unseen, a message meant for those who dare to find it. 
    Information is a key, but only those who search will unlock its meaning. Guard it well."""
    
    hide_message(input_image, output_image, secret_message)

elif choice == "2":
    stego_image = input("Enter the name of the stego image (e.g., stego_image.png): ")
    output_text_file = "extracted_message.txt"
    
    reveal_message(stego_image, output_text_file)

else:
    print("⚠ Invalid choice. Please enter 1 or 2.")
