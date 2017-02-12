import abc

from skimage.color.colorconv import rgb2gray
from skimage.filters import sobel
from skimage.morphology import watershed


class Selection(object):

    def __init__(self, image_id, image):
        self._image_id = image_id
        self._image = image
        self._classes = {}

        pass

    @property
    def image_id(self):
        return self._image_id

    @property
    def image(self):
        return self._image

    @property
    def classes(self):
        return self._classes


class PixelAnnotationOperator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self, image, pixel_annotation):
        """

        :param image: numpy.ndarray
        :param pixel_annotation: PixelAnnotation

        :returns numpy.ndarray
        """
        pass


    def run(self, image, selection_mask):
class FloodFillExpander(PixelAnnotationOperator):
        grayscale_image = rgb2gray(image)
        elevation_map = sobel(grayscale_image)
        return watershed(elevation_map, selection_mask, connectivity=[[1, 1, 1], [1, 0, 1], [1, 1, 1]])
