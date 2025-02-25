import os
from stegano import lsb

def hide_message():
    """ Hide a secret message inside an image """
    image_path = input("Enter the image file path (PNG/JPG): ")
    if not os.path.exists(image_path):
        print("❌ File not found!")
        return

    secret_message = input("🔑 Enter the secret message to hide: ")

    # Save the stego image
    stego_image_path = "stego_image.png"
    stego_image = lsb.hide(image_path, secret_message)
    stego_image.save(stego_image_path)

    print(f"✅ Secret message hidden successfully in: {stego_image_path}")

def reveal_message():
    """ Extract the hidden message from the image """
    image_path = input("Enter the stego image file path (PNG/JPG): ")
    if not os.path.exists(image_path):
        print("❌ File not found!")
        return

    try:
        hidden_text = lsb.reveal(image_path)
        print("🔍 Hidden Message:", hidden_text if hidden_text else "No hidden message found.")
    except Exception as e:
        print("❌ Error extracting message:", e)

def main():
    """ Main function to choose an option """
    while True:
        print("\n🔹 Image Steganography 🔹")
        print("1️⃣ Hide a Secret Message")
        print("2️⃣ Extract Hidden Message")
        print("3️⃣ Exit")

        choice = input("Select an option (1/2/3): ")
        
        if choice == "1":
            hide_message()
        elif choice == "2":
            reveal_message()
        elif choice == "3":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
