import hashlib
import time
import pyperclip

def hashcopy(output):
    pyperclip.copy(output)
    print("Copied to clipboard!")
    time.sleep(1)
    print("\n")

def sha256():
    string = input("Enter string to hash (SHA256): ")
    output = hashlib.sha256(string.encode()).hexdigest()
    print(output)
    hashcopy(output)

def sha512():
    string = input("Enter string to hash (SHA512): ")
    output = hashlib.sha512(string.encode()).hexdigest()
    print(output)
    hashcopy(output)

def sha1():
    string = input("Enter string to hash (SHA1): ")
    output = hashlib.sha1(string.encode()).hexdigest()
    print(output)
    hashcopy(output)

while 1:
    number = input("Choose SHA:\n1. sha256\n2. sha512\n3. sha1\n==> ")

    if number == '1':
        sha256()

    elif number == '2':
        sha512()

    elif number == '3':
        sha1()

    else:
        print("Enter a valid number ")
        time.sleep(1)
        print("\n")
