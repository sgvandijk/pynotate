import abc


class SelectionOperator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self, image, selection_mask):
        pass


class FloodFillExpander(SelectionOperator):
    def run(self, image, selection_mask):

        pass