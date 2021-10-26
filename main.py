# https://realpython.com/python-gui-tkinter/
# https://www.geeksforgeeks.org/python-grid-method-in-tkinter/

import tkinter as tk

class MasterWindow:

    def __init__(self, master=None):
        self.master = master
        master.title('MPQrcode')

        w = 700
        h = 700
        ws = master.winfo_screenwidth()
        hs = master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        master.geometry("{}x{}+{}+{}".format(w, h, int(x), int(y)))

        # LABEL
        lblTitle = tk.Label(master, text="Scegli cosa inserire")
        lblTitle.config(font=("Courier", 30))
        lblTitle.grid(row=0, column=0, sticky='W', pady=20)

        # RADIO
        self.radioValue = tk.StringVar()
        radioFoto = tk.Radiobutton(master, text='foto', value='foto', variable=self.radioValue)
        radioFoto.grid(row=1, column=0, sticky='W', pady=20)
        rdioUrl = tk.Radiobutton(master, text='url', value='url', variable=self.radioValue)
        rdioUrl.grid(row=1, column=1, sticky='W', pady=20)

        # BUTTON
        button = tk.Button(text="Scegli!", width=25, height=5, command=self.buttonClick)
        button.grid(row=2, column=0, sticky='W', pady=20)

        master.resizable(0, 0)

    def buttonClick(self):
        print(self.radioValue)

if __name__ == '__main__':
    master = tk.Tk()
    gui = MasterWindow(master)
    master.mainloop()
