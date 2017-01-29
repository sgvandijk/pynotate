from skimage.io import imread


def read_image(path, keep_alpha=False):
    """reads image from disk

    :param path: image file path
    :param keep_alpha: whether to keep or discard alpha channel if present

    :type path: str
    :type keep_alpha: bool

    :return: the loaded image
    :rtype: numpy.ndarray
    """
    image = imread(path)
    if image.shape[2] > 3 and not keep_alpha:
        image = image[:, :, :3]
    return image