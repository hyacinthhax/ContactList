from tkinter import *
import gpg
import logging
import random
import os
import gpg

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?></';|][=-()*&^%$#@!`~"


def generator():
    passlen = 35
    password = ""
    for x in range(0, passlen):
        password_char = random.choice(chars)
        password = password + password_char
    print("Here is your Password:  %s" % (password))
    logger.info("User Generated a Password for %s." % (fn))
    return password


global logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="Contacts.log",
                    level=logging.DEBUG, format=LOG_FORMAT)
logger = logging.getLogger()


def new():
    ft = input("What will the File be Called? \n (Will Format to Lowercase) \n (This Will OVERWRITE Files of the SAME NAME) \n Quit To Exit Clean:  ").lower()
    if ft == "quit":
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        global fu, fp, fn, com, ex
        fn = ft + ".txt"
        print(fn)
        com = input("Contact Name: ")
        fu = input("Contact Primary EMail:  ")
        fp = input("Contact Secondary EMail:  ")
        ex = input("Extra Details:  ")
        pw = input("Do You Need a Password For this Person ONLY?(35)(Y/N): ").lower()
        if pw == "y":
            generator()
            input("Enter To Encryption and End... THIS WILL CLEAR!!")
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Refresh Bro...")
            create()

        else:
            input("Enter To Encryption and End... THIS WILL CLEAR!!")
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Refresh Bro...")
            create()


def encryption():
    a_key = "537FD141175C3862C3B0BB1509214DB5BCCBE642"
    with open(fn, "rb") as afile:
        text = afile.read()
        c = gpg.core.Context(armor=True)
        rkey = list(c.keylist(pattern=a_key, secret=False))
        ciphertext, result, sign_result = c.encrypt(text, recipients=rkey,
                                                    always_trust=True,
                                                    add_encrypt_to=True)
    with open("{0}.asc".format(fn), "wb") as bfile:
        bfile.write(ciphertext)
        logger.info("User Made a New File: %s" % (fn))
    os.remove(fn)
    


def create():
    with open(fn, 'w+') as filen:
        text = str(com + '\n' + fu + '\n' + fp + '\n' + ex)
        filen.write(text)
    encryption()
