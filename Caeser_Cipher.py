"""
Encrypting or decrypting a message using the ceaser cipher.

text(str): the message to be encypted or decrypted
shift(int): the number of position to shift the letters.
encrypt(bool): whether to encryot or decrypt default is true  
"""
#implement the caeeser cipher 
def caesar_cipher(text, shift, encrypt = True):
    result = ""

    if not encrypt:
        # shift the position to the letter to the opposite direction 
        shift = -shift

    # Iterate through each character in the input text
    for char in text:
        #check if character is an uppercase letter 
        if char.isupper():
            '''
            calculate the ASCII value of the shifted character (A to Z) = (65 to 90)
            We subtract 65 to shift the range to 0 to 25, add the shift, take the modulus to wrap around, and then add 65 back
            '''
            result += chr(ord(char) + shift - 65) % 26 + 65
        # cheak if character us a lowercase letter 
        elif char.islower():
            '''
            calculate the ASCII value of the shifted character (a to z) = (97 to 122)
            We subtract 97 to shift the range to 0 to 25, add the shift, take the modulus to wrap around, and then add 97 back
            '''
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # if the is not a letter leave is unchanged 
            result += char
    # return the encrypted or decrypted message 
    return result
  

if __name__ == "__main__":
    # Receive inputs from user   
    message = input("Enter message: ")  
    shift = int(input("Enter the shift value: "))
    action = input("Type 'e' to encrypt or 'd' to decrypt: ").strip().lower()       

# Perform the chosen action
    if action == 'e':
        # Encrypt the message
        encrypted_message = caesar_cipher(message, shift, encrypt=True)
        print("Encrypted Message:", encrypted_message)
    elif action == 'd':
        # Decrypt the message
        decrypted_message = caesar_cipher(message, shift, encrypt=False)
        print("Decrypted Message:", decrypted_message)
    else:
        # Handle invalid input
        print("Invalid action. Please choose 'e' or 'd'.") 