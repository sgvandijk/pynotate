import abc
import tkinter as tk

from PIL import Image
from PIL import ImageTk


class AnnotatedImageView(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def image(self):
        pass

    @abc.abstractproperty
    def annotation(self):
        pass


class TKAnnotatedImageView(AnnotatedImageView):
    def __init__(self):
        self._image = None
        self._annotation = None
        self._panel = tk.Label()

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
        self._photo_image = ImageTk.PhotoImage(Image.fromarray(self._image))
        self._panel.config(width=self._image.shape[1], height=self._image.shape[0],
                           image=self._photo_image)

    @property
    def annotation(self):
        return self._annotation

    @property
    def panel(self):
        return self._panel
