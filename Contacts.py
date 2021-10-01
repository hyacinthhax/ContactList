import gpg
import os
from crypto import *
from tkinter import *

# Setup
root = Tk()
tItle = "Contact-List"
root.title(tItle)
root.geometry("400x700")
c = gpg.Context()
recipient = c.get_key("38DEA3AC606FFCCAEAEFEF1B5B91BC78766AD69A")

restrictedfiles = []
with open('restrictedfiles.txt') as f:
    data = []
    for datas in f.readlines():
        data.append(datas)
    for line in data:
        restrictedfiles.append(line.strip('\n'))

# List Box
def refresh():
    global listBox
    files = []
    for file in os.listdir(os.getcwd()):
        if file not in restrictedfiles:
            files.append(file)
    listBox = Listbox(root, width=40, height=33)
    listBox.grid(row=1, column=0, columnspan=5, rowspan=9)
    for item in files:
        listBox.insert(END, item)

# Entry
e = Entry(root, width=40, borderwidth=3)
e.grid(row=0, column=0, columnspan=9)
decryptEntry = Entry(root, width=40, borderwidth=3)
decryptEntry.grid(row=15, column=0)
# Label
labelData = Label(root, text="Made by: Hyacinthhax")
labelData.grid(row=20, column=0)

def decryptFile():
    fn = str(listBox.get(ANCHOR))
    with open("{0}".format(fn), "rb") as cfile:
        plaintext, result, verify_result = gpg.Context().decrypt(cfile)
        decryptEntry.insert(0, plaintext)
        logger.info("User Viewed/Decrypted %s" % (fn))
        print("CLEAR THE TEXT FIELD WHEN DONE...  ")


def delete():
    os.remove(listBox.get(ANCHOR))
    listBox.delete(ANCHOR)


def search():
    pass


# Buttons
button_quit = Button(root, text="Exit", command=root.quit)
button_Delete = Button(root, text="Delete", command=delete)
button_Search = Button(root, text="Search", command=search)
button_New = Button(root, text="Add", command=new)
button_Decrypt = Button(root, text="View", command=decryptFile)
button_Refresh = Button(root, text="Refresh", command=refresh)


# Buttons to Grid
button_quit.grid(row=20, column=10)
button_Delete.grid(row=2, column=10)
button_Search.grid(row=0, column=10)
button_New.grid(row=3, column=10)
button_Decrypt.grid(row=4, column=10)
button_Refresh.grid(row=5, column=10)

# End Loop
refresh()
root.mainloop()
