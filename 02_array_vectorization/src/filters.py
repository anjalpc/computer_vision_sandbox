import numpy as np

def box_filter_loop(img: np.ndarray, box_width: int, box_height: int) -> np.ndarray:
    """
    Computes a box filter using naive nested loops.
    Time Complexity: O(f^2 * n^2)
    """
    box_size = box_width * box_height
    result = np.zeros([img.shape[0] - (box_height - 1), img.shape[1] - (box_width - 1)])

    # Iterate over the image
    for result_y in range(result.shape[0]):
        for result_x in range(result.shape[1]):
            local_sum = 0.0

            # Sum up the image pixels covered by the box filter
            for filter_y in range(result_y, result_y + box_height):
                for filter_x in range(result_x, result_x + box_width):
                    local_sum += img[filter_y, filter_x]

            result[result_y, result_x] = local_sum / box_size
    return result


def box_filter_vectorized(img: np.ndarray, box_width: int, box_height: int) -> np.ndarray:
    """
    Computes a box filter using vectorized image slicing.
    Time Complexity: O(f^2 * n^2) with optimized C-level slicing execution.
    """
    box_size = box_width * box_height
    result = np.zeros([img.shape[0] - (box_height - 1), img.shape[1] - (box_width - 1)])

    # Iterate over the box filter window offsets
    for filter_y in range(box_height):
        for filter_x in range(box_width):
            # Sum up the sliced 2D arrays covered by the filter
            result += img[filter_y : filter_y + result.shape[0], 
                          filter_x : filter_x + result.shape[1]]

    return result / box_size


def box_filter_integral(img: np.ndarray, box_width: int, box_height: int) -> np.ndarray:
    """
    Computes a box filter in constant time per pixel using an Integral Image.
    Time Complexity: O(n^2) - independent of filter size f.
    """
    box_size = box_width * box_height

    # 1. Compute the integral image (summed-area table)
    integral_image = img.cumsum(axis=0).cumsum(axis=1)

    # 2. Pad the integral image with zeros on the top and left boundaries
    # to guarantee that the box filter calculations work at the borders.
    integral_image = np.pad(integral_image, ((1, 0), (1, 0)), mode='constant', constant_values=0)

    # 3. Retrieve coordinates. (Note: shape returns (height, width))
    h, w = integral_image.shape
    
    top_left = integral_image[0 : h - box_height, 0 : w - box_width]
    bottom_right = integral_image[box_height : h, box_width : w]
    top_right = integral_image[0 : h - box_height, box_width : w]
    bottom_left = integral_image[box_height : h, 0 : w - box_width]
    
    # 4. Apply the O(1) box sum formula: A + D - B - C
    result = (top_left + bottom_right - top_right - bottom_left) / box_size
    return result


if __name__ == "__main__":
    import urllib.request
    import cv2
    import matplotlib
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt

    url = 'https://dome.mit.edu/bitstream/handle/1721.3/195767/cameraman.tif.jpg?sequence=4&isAllowed=y'
    print("Downloading test image from MIT...")
    try:
        with urllib.request.urlopen(url) as resp:
            img = np.asarray(bytearray(resp.read()), dtype="uint8")
            img = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)
    except Exception as e:
        print(f"Could not download image: {e}")
        # fallback to random noise
        img = (np.random.rand(256, 256) * 255).astype(np.uint8)

    def show(img):
        if type(img) == list:
            img = np.concatenate(img, axis=1)
        if len(img.shape) == 2:
            plt.imshow(img, cmap="gray")
        else:
            plt.imshow(cv2.cvtColor((img * 255).astype(np.uint8), cv2.COLOR_BGR2RGB))
        plt.show()

    print("Running filter implementations (5x5 box filter)...")
    naive = box_filter_loop(img, 5, 5)
    vectorized = box_filter_vectorized(img, 5, 5)
    integral = box_filter_integral(img, 5, 5)

    print("Displaying notebook comparison (Original | Naive | Vectorized | Diff^2)...")
    plt.figure(figsize=(12, 4))
    show([img[2:-2, 2:-2], naive, vectorized, (naive - vectorized)**2])
