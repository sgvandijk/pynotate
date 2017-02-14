import abc
import tkinter.ttk as ttk

class AnnotationClassView(metaclass=abc.ABCMeta):

    @abc.abstractproperty
    def classes(self):
        pass


class TKAnnotationClassView(AnnotationClassView):
    def __init__(self):
        self._classes = []
        columns = ['label']
        self._tree_view = ttk.Treeview(columns=columns)
        for c in columns:
            self._tree_view.heading(c, text=c.capitalize())
        self._current_items = []

    @property
    def tree_view(self):
        return self._tree_view

    @property
    def classes(self):
        return self._classes

    @classes.setter
    def classes(self, value):
        self._classes = value
        self._update_tree_view()

    def _update_tree_view(self):
        self._tree_view.delete(*self._current_items)
        self._current_items = []
        for c in self._classes:
            id = self._tree_view.insert('', 'end', text=c.name, values=(c.label, c.color), tags=(c.name))
            self._tree_view.tag_configure(c.name, foreground=c.color)
            self._current_items.append(id)
