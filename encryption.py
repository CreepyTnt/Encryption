from cryptography.fernet import Fernet
import os

key = Fernet.generate_key() 
fernet = Fernet(key)


def save_key(location):
    if os.path.isdir(location):
        with open(os.path.join(location, 'key.txt'), 'wb') as f:
            f.write(key)
    elif os.path.isfile(location):
        with open(location, 'wb') as f:
            f.write(key)
    else:
        raise ValueError(f'path: "{location}" is not a valid path')

def load_key_from_file(location):
    with open(location, 'rb') as f:
        fernet = Fernet(f.read())

def import_key(key):
    fernet = Fernet(key)

def import_key(input_key):
    fernet = Fernet(input_key)

def encreypt(message):

    encMsg = fernet.encrypt(message.encode())
    return(encMsg)
    # print("original string: ", message)
    # print("encrypted string: ", encMsg)
 
def decrypt(encrypted):
    decMessage = fernet.decrypt(encrypted).decode()
    return(decMessage)
#print("decrypted string: ", decMessage)

