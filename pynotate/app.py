import tkinter as tk


class Application(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, master=None)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.quitButton = tk.Button(self, text='Quit',
                                    command=self.quit)
        self.quitButton.grid()


if __name__ == '__main__':
    app = Application()
    app.master.title('Pynotate')
    app.mainloop()
