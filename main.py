from tkinter import *
from Genrator import Generator


class Main:
    width, height = 400, 400

    def __init__(self):
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

        self.create_mdp = Button(self.frame, text="Générer un MDP", bg=self.bg, fg="white", border=1,
                                 height=int(self.height / 130), width=int(self.width / 12.5), font=0, command=self.generate).pack()

        self.frame.pack()

    def generate(self):
        self.window.destroy()
        Generator()


Main()
