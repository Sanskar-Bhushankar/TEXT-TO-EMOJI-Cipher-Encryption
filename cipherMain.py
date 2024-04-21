from emojiFinal import emoji
from emojiFinal import dec

def encryption(plainText, key):
    temp_dec = ""
    key_list = []

    if len(key) >= len(plainText):
        print("Error: The length of the key should be smaller than the length of the plainText.")
          # You may choose to return an error code or handle the error in a different way.

    key_repeated = key * (len(plainText) // len(key)) + key[:len(plainText) % len(key)]

    for x in key_repeated:
        ascii_values_key = ord(x)
        key_list.append(ascii_values_key)

    plainText_list = []
    for char in plainText:
        ascii_values_pt = ord(char)
        plainText_list.append(ascii_values_pt)

    result_stream = []
    back_fire_ascii_stream = []
    
    for a, b in zip(plainText_list, key_list):
        result = (a + b) % 127
        result_stream.append(result)
        back_fire_ascii = chr(result)
        back_fire_ascii_stream.append(back_fire_ascii)

    back_fire_ascii_string = ''.join(back_fire_ascii_stream)

    temp_dec = emoji(back_fire_ascii_string)
    return temp_dec

def decryption(temp_dec, key):
    key_list = []

    if len(key) < len(temp_dec):
        key_repeated = key * (len(temp_dec) // len(key)) + key[:len(temp_dec) % len(key)]

        for x in key_repeated:
            ascii_values_key = ord(x)
            key_list.append(ascii_values_key)

    result_plainText = []

    for a, b in zip(temp_dec, key_list):
        result = (ord(a) - b + 127) % 127
        result_char = chr(result)
        result_plainText.append(result_char)

    return result_plainText

# Get input from the user
plainText = input("Enter plain Text: ")
key = input("Enter Key: ")

# Call the encryption function and get the result
cipherText = encryption(plainText, key)

# Call the decryption function and get the result
decrypted_plainText = decryption(cipherText, key)
print("Decrypted Plain Text:", ''.join(decrypted_plainText))
