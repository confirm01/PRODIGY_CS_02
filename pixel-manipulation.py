
from PIL import Image
import numpy as np
import argparse

def encrypt_image(input_path, output_path, key):
    """
    Encrypt an image by performing pixel value manipulation
    """
    try:
        # Open the image
        img = Image.open(input_path)
        pixels = np.array(img)
        
        # Simple encryption algorithm: XOR each pixel value with the key
        encrypted_pixels = pixels ^ key
        
        # Save the encrypted image
        encrypted_img = Image.fromarray(encrypted_pixels)
        encrypted_img.save(output_path)
        print(f"Image encrypted and saved to {output_path}")
        
    except Exception as e:
        print(f"Error during encryption: {e}")

def decrypt_image(input_path, output_path, key):
    """
    Decrypt an image (same operation as encryption for XOR)
    """
    try:
        # Open the encrypted image
        img = Image.open(input_path)
        pixels = np.array(img)
        
        # Decryption is the same as encryption for XOR operation
        decrypted_pixels = pixels ^ key
        
        # Save the decrypted image
        decrypted_img = Image.fromarray(decrypted_pixels)
        decrypted_img.save(output_path)
        print(f"Image decrypted and saved to {output_path}")
        
    except Exception as e:
        print(f"Error during decryption: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple Image Encryption Tool")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt")
    parser.add_argument("input", help="Input image path")
    parser.add_argument("output", help="Output image path")
    parser.add_argument("key", type=int, help="Encryption/decryption key (integer)")
    
    args = parser.parse_args()
    
    if args.mode == "encrypt":
        encrypt_image(args.input, args.output, args.key)
    else:
        decrypt_image(args.input, args.output, args.key)

if __name__ == "__main__":
    main()

Image-encrypt-&-decrypty.py
Displaying Image-encrypt-&-decrypty.py.
