# https://realpython.com/python-gui-tkinter/
# https://www.geeksforgeeks.org/python-grid-method-in-tkinter/

import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.title('MPQrcode')

    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)
    root.geometry("{}x{}+{}+{}".format(700, 700, positionRight, positionDown))

    lblTitle = tk.Label(root, text="Scegli cosa inserire")
    lblTitle.grid(row=0, column=0, sticky='W', pady=2)

    root.resizable(0, 0)
    root.mainloop()
