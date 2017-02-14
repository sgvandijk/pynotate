import tkinter as tk

from pynotate.io import read_image
from pynotate.view.annotatedimageview import TKAnnotatedImageView


class Application(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, master=None)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.image_view = TKAnnotatedImageView()
        self.image_view.panel.grid()

        img = read_image('tests/resources/colors.png')
        self.image_view.image = img

        self.quitButton = tk.Button(self, text='Quit',
                                    command=self.quit)
        self.quitButton.grid()


if __name__ == '__main__':
    def check():
        app.after(50, check)

    app = Application()
    app.master.title('Pynotate')
    app.after(50, check)
    try:
        app.mainloop()
    except KeyboardInterrupt:
        pass
