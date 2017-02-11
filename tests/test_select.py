import unittest
import numpy as np
from skimage.io._io import imshow, imsave

from pynotate.io import read_image
from pynotate.select import FloodFillExpander


class TestSelect(unittest.TestCase):
    def test_floodfill_expander_single_label(self):
        # When only a single label is given, the full image should be selected

        image = read_image('resources/colors.png')
        initial_selection_mask = np.zeros(image.shape[:2])

        # Select one pixel in brightest red area
        initial_selection_mask[20, 20] = 1

        expander = FloodFillExpander()

        new_selection_mask = expander.run(image, initial_selection_mask)
        self.assertEqual(new_selection_mask.shape, initial_selection_mask.shape)

        expected_selection_mask = np.zeros(image.shape[:2])
        expected_selection_mask[:, :] = 1
        np.testing.assert_array_equal(expected_selection_mask, new_selection_mask)

    def test_floodfill_expander_white_background(self):
        # With a selection in the white background, selection should cover coloured squares

        image = read_image('resources/colors.png')
        initial_selection_mask = np.zeros(image.shape[:2])

        # Select one pixel in brightest red area
        initial_selection_mask[40, 40] = 1

        # Select one pixel white with another label
        initial_selection_mask[120, 40] = 2

        expander = FloodFillExpander()
        new_selection_mask = expander.run(image, initial_selection_mask)

        self.assertEqual(new_selection_mask.shape, initial_selection_mask.shape)

        expected_selection_mask = np.zeros(image.shape[:2])
        expected_selection_mask[:, :] = 2
        expected_selection_mask[20:60, 20:180] = 1
        np.testing.assert_array_equal(expected_selection_mask, new_selection_mask)
