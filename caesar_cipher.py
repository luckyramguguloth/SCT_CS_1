"""
Task 01: Caesar Cipher Tool
SkillCraft Technology Cybersecurity Internship

This script implements a command-line Caesar Cipher encryption and decryption tool.
It safely processes alphabetic characters, handles wrap-arounds, maintains case sensitivity,
and leaves numeric and punctuation symbols untouched.
"""

import sys

def caesar_cipher(text: str, shift: int, mode: str) -> str:
    if mode.lower() == 'decrypt':
        shift = -shift
    
    normalized_shift = shift % 26
    result = []
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr(base + (ord(char) - base + normalized_shift) % 26)
            result.append(new_char)
        else:
            result.append(char)
            
    return "".join(result)


def print_banner():
    """Prints a styled terminal banner."""
    print("=" * 60)
    print("              CAESAR CIPHER ENCRYPTION/DECRYPTION TOOL         ")
    print("=" * 60)


def main():
    print_banner()
    while True:
        try:
            print("\nSelect an option:")
            print("1) Encrypt a message")
            print("2) Decrypt a message")
            print("3) Exit")
            choice = input("Enter choice (1-3): ").strip()
            
            if choice == '3':
                print("\nThank you for using the Caesar Cipher Tool. Goodbye!")
                break
                
            if choice not in ('1', '2'):
                print("[!] Invalid choice. Please enter 1, 2, or 3.")
                continue
                
            mode = 'encrypt' if choice == '1' else 'decrypt'
            message = input(f"\nEnter the message to {mode}: ")
            
            shift_input = input("Enter the shift key (integer): ").strip()
            try:
                shift = int(shift_input)
            except ValueError:
                print("[!] Invalid key. Shift key must be an integer.")
                continue
                
            processed = caesar_cipher(message, shift, mode)
            print("-" * 60)
            print(f"Resulting {mode}ed message:")
            print(processed)
            print("-" * 60)
            
        except (KeyboardInterrupt, EOFError):
            print("\n\nOperation cancelled. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()
