import abc

from skimage.color.colorconv import rgb2gray
from skimage.filters import sobel
from skimage.morphology import watershed


class SelectionOperator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self, image, selection_mask):
        """

        :param image: numpy.ndarray
        :param selection_mask: numpy.ndarray

        :returns numpy.ndarray
        """
        pass


class FloodFillExpander(SelectionOperator):
    def run(self, image, selection_mask):
        grayscale_image = rgb2gray(image)
        elevation_map = sobel(grayscale_image)
        return watershed(elevation_map, selection_mask, connectivity=[[1, 1, 1], [1, 0, 1], [1, 1, 1]])
