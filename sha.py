import hashlib
import time
import pyperclip
import subprocess as sp


# copy hash to clipboard
def hash_copy(output):
    pyperclip.copy(output)
    print("Copied to clipboard!")
    time.sleep(2)
    print("\n")


# show output
def call(string, output):
    sp.call('clear', shell=True)
    print("Input:", string)
    print("Hash: ", output)
    hash_copy(output)


def sha256():
    string = input("Enter string to hash (SHA256): ")
    output = hashlib.sha256(string.encode()).hexdigest()
    call(string, output)


def sha512():
    string = input("Enter string to hash (SHA512): ")
    output = hashlib.sha512(string.encode()).hexdigest()
    call(string, output)


def sha1():
    string = input("Enter string to hash (SHA1): ")
    output = hashlib.sha1(string.encode()).hexdigest()
    call(string, output)


def md5():
    string = input("Enter string to hash (MD5): ")
    output = hashlib.md5(string.encode()).hexdigest()
    call(string, output)


def sha224():
    string = input("Enter string to hash (SHA224): ")
    output = hashlib.sha224(string.encode()).hexdigest()
    call(string, output)


def sha384():
    string = input("Enter string to hash (SHA384): ")
    output = hashlib.sha384(string.encode()).hexdigest()
    call(string, output)


while 1:
    number = input(
        "Secure Hash Algorithm list:\n1. sha256\n2. sha512\n3. sha1\n4. sha224\n5. sha384\n6. md5\nEnter number: ")

    if number == '1':
        sha256()

    elif number == '2':
        sha512()

    elif number == '3':
        sha1()

    elif number == '4':
        sha224()

    elif number == '5':
        sha384()

    elif number == '6':
        md5()

    else:
        print("Enter a valid number ")
        time.sleep(1)
        print("\n")
