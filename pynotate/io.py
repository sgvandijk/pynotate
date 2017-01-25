from skimage.io import imread


def read_image(path, keep_alpha=False):
    image = imread(path)
    if image.shape[2] > 3 and not keep_alpha:
        image = image[:, :, :3]
    return image