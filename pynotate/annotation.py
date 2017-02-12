import abc
import json

import numpy as np
from skimage.color.colorconv import rgb2gray
from skimage.filters import sobel
from skimage.morphology import watershed


class Annotation(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def as_layer(self):
        pass

    @abc.abstractmethod
    def to_json(self):
        pass

    @abc.abstractclassmethod
    def from_json(cls, json):
        pass


class AnnotationSet(object):
    def __init__(self, image_id, image):
        self._image_id = image_id
        self._image = image
        self._classes = {}
        self._annotations = []

    @property
    def image_id(self):
        return self._image_id

    @property
    def image(self):
        return self._image

    @property
    def classes(self):
        return self._classes

class PixelAnnotation(Annotation):
    def __init__(self, annotation_mask=None):
        self._annotation_mask = annotation_mask

    @property
    def annotation_mask(self):
        return self._annotation_mask

    def as_layer(self):
        return self._annotation_mask

    def to_json(self):
        return json.dumps({'mask': self.annotation_mask.tolist()})

    @classmethod
    def from_json(cls, json_str):
        return PixelAnnotation(np.array(json.loads(json_str)['mask']))


class PixelAnnotationOperator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self, image, pixel_annotation):
        """

        :param image: numpy.ndarray
        :param pixel_annotation: PixelAnnotation

        :returns numpy.ndarray
        """
        pass


class FloodFillExpander(PixelAnnotationOperator):
    def run(self, image, pixel_annotation):
        grayscale_image = rgb2gray(image)
        elevation_map = sobel(grayscale_image)
        new_annotation_mask = watershed(elevation_map, pixel_annotation.as_layer(),
                                        connectivity=[[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        return PixelAnnotation(new_annotation_mask)
