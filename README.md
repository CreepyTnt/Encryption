# Encryption
A very simple example module for fernet encryption and encryption.

# Installation
Simply clone the repo and import encryption into your project:
```python
import encryption
```


#Keys
A new key is generated when you run the program however, you can load a key from a file like this:
```python
encryption.load_key_from_file('path/to/file/')
```

You can also load a key as a string like this:
``` python
encryption.import_key(your_key)
```

You can also save keys like this:
```python
encryption.save_key('directory/to/save') # if you don't provide the file name, a file "key.txt" will be automatically created. If "key.txt" or the provided file already exists, it will be over-written
```

#Encrypting data
```python
message = 'hello world
encrypted = encryption.encrypt(message)
with open('path/to/save/file', 'wb') as f:
  f.write(encrypted)
```


#Decrypting data
This is where things start to get different. You will need to import the correct key before you can start decrypting.
```python
encryption.load_key(path/to/file/')
```
after you import the key, you can actually decrypt things like this:
```python
encrypted = ''
with open('path/to/encrypted/file', 'rb') as f:
  encrypted = f.read()
print (encryption.decrypt(encrypted))
