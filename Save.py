from tkinter import *


class Save:
    width, height = 400, 400
    def __init__(self, mdp):
        self.mdp = mdp
        self.window = Tk()
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False, False)
        self.bg = "#458ECF"
        self.window.config(bg=self.bg)

        img = PhotoImage(file="images/logo.png")
        canvas = Canvas(self.window, width=self.width / 1.5, height=self.height / 1.5, bg=self.bg, highlightthickness=0)
        canvas.create_image(137, 137, image=img)

        canvas.pack()

        self.run()

        self.window.mainloop()

    def run(self):
        self.frame = Frame(self.window, bg=self.bg)
        Label(self.frame, text='Site (lien)', bg=self.bg, fg="white").grid(row=0, column=0)
        self.entry_site = Entry(self.frame, font=('', 17)).grid(row=0, column=1)

        self.frame.pack()
        Button(self.window, text="Save", bg=self.bg, border=0, height=int(self.height/120), width=int(self.width/10)).pack()