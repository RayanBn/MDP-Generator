from tkinter import *
import random
from Save import Save


class Generator:
    width, height = 400, 400
    def __init__(self):
        self.window = Tk()
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False, False)
        self.bg = "#458ECF"
        self.window.config(bg= self.bg)

        img = PhotoImage(file="images/logo.png")
        canvas = Canvas(self.window, width=self.width / 1.8, height=self.height / 1.8, bg=self.bg, highlightthickness=0)
        canvas.create_image(115, 120, image=img)

        canvas.pack()

        self.run()

        self.window.mainloop()

    def run(self):
        self.frame = Frame(self.window, bg=self.bg)
        Label(self.frame, text="Voici votre mot de passe :", font=("", 15), bg=self.bg, fg="white").pack()
        self.generate()

        self.button_frame = Frame(self.window, bg=self.bg)
        Button(self.button_frame, text="New", command=self.new, height=int(self.height / 150), width=int(self.width / 20), bg=self.bg, border=0).grid(row=0, column=0)
        Button(self.button_frame, text="Save", command=self.save, height=int(self.height / 150), width=int(self.width / 20), bg=self.bg, border=0).grid(row=0, column=1)

        self.frame.pack()
        self.button_frame.pack()

    def generate(self):
        size = random.randint(10, 15)
        mdp_list = []
        for i in range(size):
            lettre = random.randint(33, 126)
            lettre = chr(lettre)
            mdp_list.append(lettre)
        self.mdp = "".join(mdp_list)
        entry_mdp = Entry(self.frame, bg=self.bg, font=("", 20))
        entry_mdp.insert(0, self.mdp)
        entry_mdp.pack()

    def new(self):
        self.window.destroy()
        Generator()

    def save(self):
        self.window.destroy()
        Save(self.mdp)