import unittest

from pynotate.io import read_image


class TestIO(unittest.TestCase):

    def test_read_image(self):
        image = read_image('resources/20160430-17:33:03.png')
        self.assertEqual((480, 640, 3), image.shape)

        image = read_image('resources/colors.png')
        self.assertEqual((200, 200, 3), image.shape)

        image = read_image('resources/colors.png', keep_alpha=True)
        self.assertEqual((200, 200, 4), image.shape)
