import numpy as np
from typing import List, Tuple
import cv2
import os

t_image_list = List[np.array]
t_str_list = List[str]
t_image_triplet = Tuple[np.array, np.array, np.array]


def show_images(images: t_image_list, names: t_str_list) -> None:
    """Shows one or more images at once.

    Displaying a single image can be done by putting it in a list.

    Args:
        images: A list of numpy arrays in opencv format [HxW] or [HxWxC]
        names: A list of strings that will appear as the window titles for each image

    Returns:
        None
    """
    for image, name in zip(images, names):
        cv2.imshow(name, image)

    cv2.waitKey(0)


def save_images(images: t_image_list, filenames: t_str_list, **kwargs) -> None:
    """Saves one or more images at once.

    Saving a single image can be done by putting it in a list.

    Args:
        images: A list of numpy arrays in opencv format [HxW] or [HxWxC]
        filenames: A list of strings where each respective file will be created

    Returns:
        None
    """
    for image, filename in zip(images, filenames):
        folder = os.path.dirname(filename)

        if folder:
            os.makedirs(folder, exist_ok=True)

        cv2.imwrite(filename, image)


def scale_down(image: np.array) -> np.array:
    """Returns an image half the size of the original.

    Args:
        image: A numpy array with an opencv image

    Returns:
        A numpy array with an opencv image half the size of the original image
    """
    height, width = image.shape[:2]

    small_image = cv2.resize(
        image,
        (width // 2, height // 2),
        interpolation=cv2.INTER_NEAREST_EXACT
    )

    return small_image


def separate_channels(colored_image: np.array) -> t_image_triplet:
    """Takes a BGR color image and splits it into three images.

    Args:
        colored_image: A numpy array sized [HxWxC] where the channels are in BGR order.

    Returns:
        A tuple with three BGR images:
        - first image: only blue channel active
        - second image: only green channel active
        - third image: only red channel active
    """
    blue = np.zeros_like(colored_image)
    green = np.zeros_like(colored_image)
    red = np.zeros_like(colored_image)

    blue[:, :, 0] = colored_image[:, :, 0]
    green[:, :, 1] = colored_image[:, :, 1]
    red[:, :, 2] = colored_image[:, :, 2]

    return blue, green, red