# Task 01: Caesar Cipher Tool

An interactive command-line interface tool implemented in Python to encrypt and decrypt text using the classic Caesar Cipher algorithm.

## Features
*   **Case Sensitivity**: Preserves uppercase and lowercase lettering formatting.
*   **Punctuation Preservation**: Ignores symbols, punctuation marks, numbers, and spaces so they are left untouched.
*   **Modular Math Shift Support**: Handles positive, negative, and large integer keys gracefully (e.g., a shift key of 28 is correctly normalized to a shift of 2).
*   **Simple Interactive Loop**: Allows continuous operations without restarting the script.

## Getting Started

### Prerequisites
*   Python 3.x installed.

### How to Run
Execute the script using python from your terminal:
```bash
python caesar_cipher.py
```

### Usage Example
1. Run the script.
2. Select `1` to Encrypt.
3. Message: `Hello, World! 123`
4. Shift Key: `3`
5. **Output**: `Khoor, Zruog! 123`
6. To decrypt, select `2`, paste `Khoor, Zruog! 123`, enter shift key `3`, and it will restore `Hello, World! 123`.

## Execution Result
Here is the execution demonstration showing the encryption and decryption processes:

![Execution Result](Screenshot%202026-06-01%20093956.png)

