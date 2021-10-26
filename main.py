# https://realpython.com/python-gui-tkinter/
# https://www.geeksforgeeks.org/python-grid-method-in-tkinter/

import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.title('MPQrcode')

    w = 700
    h = 700
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry("{}x{}+{}+{}".format(w, h, int(x), int(y)))

    lblTitle = tk.Label(root, text="Scegli cosa inserire")
    lblTitle.grid(row=0, column=0, sticky='W', pady=2)

    root.resizable(0, 0)
    root.mainloop()
