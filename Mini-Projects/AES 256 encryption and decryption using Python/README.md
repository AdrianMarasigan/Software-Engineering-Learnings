# AES 256 encryption and decryption using Python

## Overview:
AES (Advanced Encryption Standard) is a widely used symmetric encryption algorithm that provides secure encryption and decryption of data.

This Python script demonstrates AES-256 encryption and decryption using the pycryptodome library.  This script allows you to encrypt and decrypt messages with ease, and it includes enhanced features for testing and usability.

## How Does AES 256 Work?

AES operates on blocks of data and supports key sizes of 128, 192, and 256 bits. AES 256-bit encryption is the most secure variant of AES and provides a very high level of security.

### Key Expansion

The first step in AES 256 encryption is to expand the user-provided 256-bit encryption key into a set of round keys. This process involves performing mathematical operations on the key to generate a series of round keys that will be used in the encryption and decryption rounds.

### Initial Round

AES consists of multiple rounds, each consisting of four main transformations: SubBytes, ShiftRows, MixColumns, and AddRoundKey. In the initial round, the plaintext data is XORed (bitwise exclusive OR) with the first round key.

### Main Rounds

In the main rounds, the plaintext block goes through a series of transformations:

- **SubBytes:** Each byte of the block is replaced with a corresponding byte from a fixed substitution table (S-Box).
- **ShiftRows:** Bytes within each row of the block are shifted by varying numbers of positions.
- **MixColumns:** Each column of the block is transformed using a mathematical operation.
- **AddRoundKey:** The current round key is XORed with the block.

### Final Round

In the final round, the SubBytes and ShiftRows transformations are applied as usual, but the MixColumns transformation is omitted. The AddRoundKey operation is performed using the final round key.

### Output

After the final round, the encrypted data block is produced, which is the ciphertext. This ciphertext can be sent securely over a network or stored on a disk.

Decryption in AES 256 works in reverse. The ciphertext is subjected to a series of transformations in the reverse order, using the decryption keys generated from the original encryption key. The process produces the original plaintext.

Some key points to note about AES 256 encryption:

- AES 256 is a symmetric encryption algorithm, meaning the same key is used for both encryption and decryption.
- The security of AES 256 largely relies on the strength of the encryption key. A 256-bit key is considered extremely secure and resistant to brute force attacks.
- AES is widely used in various applications, including secure communication, data encryption, and more.
- AES encryption and decryption are highly efficient and can be implemented in hardware and software.

Overall, AES 256 is a robust encryption algorithm that plays a crucial role in securing sensitive data in many modern computing systems.


## Purpose:
The primary purpose of this script is to provide a practical example of AES encryption and decryption in Python. You can use this script to protect sensitive data by encrypting it with a strong password. The recent updates have improved user interaction and testing capabilities.

## Walkthrough of the Code:
1. **Imports and Dependencies:** The script starts by importing necessary libraries, including hashlib, base64, os, and pycryptodome modules.

2. **Clearing the Console:** It clears the console screen based on the operating system to provide a clean interface for user interaction.

3. **Encryption and Decryption Functions:**
   - `encrypt(plain_text, password)`: This function takes a plaintext message and a password as input, encrypts the message, and returns a dictionary containing the encrypted text, salt, nonce, and tag.
   - `decrypt(enc_dict, password)`: This function takes an encrypted message dictionary and a password as input, decrypts the message, and returns the original plaintext.

4. **Command-Line Interface (CLI):**
   - The `main()` function provides a command-line interface with improved usability.
   - Users can choose between encryption and decryption actions using the `encrypt` or `decrypt` command.
   - Password and message inputs can be provided as command-line arguments, making it easier to automate testing.
   - Clear error handling ensures that users receive informative messages when incorrect inputs are provided.

5. **Navigating to the Appropriate Folder:**
   - Before running the script, you may need to navigate to the appropriate folder in the command prompt or terminal. Here's how to do it:
     - Open a command prompt or terminal window.
     - Use the `cd` (Change Directory) command to navigate to the folder where the script is located. For example, if the script is in a folder named "aes-encryption," you can navigate to it using the following command:
     
       ```shell
       cd path/to/aes-encryption
       ```
     
     - Replace `path/to/aes-encryption` with the actual path to your script's folder. You can use the `cd` command followed by the folder name to move into that folder.

## How to Run the Program:
1. **Prerequisites:**
   - Ensure you have Python 3.x installed on your system.
   - Install the pycryptodome library if you haven't already. You can install it using pip:

     ```shell
     pip install pycryptodome
     ```

2. **Run the Script:**
   - Save this script as a .py file, such as `aes_encryption.py`.
   - Open a terminal or command prompt and navigate to the directory containing the script.

3. **Encryption:**
   - To encrypt a message, use the following command, providing the password:

     ```shell
     python aes_encryption.py encrypt your_password
     ```

     You will be prompted to enter the secret message interactively.

4. **Decryption:**
   - To decrypt a message, use the following command, providing the password and the encrypted message as a JSON-formatted string (enclosed in single or double quotes):

     ```shell
     python aes_encryption.py decrypt your_password
     ```

     You will be prompted to enter the encrypted message dictionary interactively. Input the dictionary as follows:

     ```shell
     Enter the encrypted message (as a dictionary): '{"cipher_text": "...", "salt": "...", "nonce": "...", "tag": "..."}'
     ```

     Replace the `"..."` placeholders with the actual values for each key from your encrypted message.

5. **View the Results:**
   - The script will display the encrypted or decrypted message, depending on your chosen action.

**Note:**
- Ensure that you keep your password safe and do not lose it. Without the correct password, you cannot decrypt the message.
- This script is for educational purposes and should not be used for critical security applications without additional security measures.
