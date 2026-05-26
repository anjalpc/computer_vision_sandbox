import sys
from pathlib import Path
import cv2

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

from utils import show_images, save_images, scale_down, separate_channels

if __name__ == "__main__":
    input_path = BASE_DIR / "resources" / "img.png"
    output_path = BASE_DIR / "results"

    img = cv2.imread(str(input_path), cv2.IMREAD_COLOR)

    if img is None:
        raise FileNotFoundError(f"Could not load image from: {input_path}")

    show_images([img], ["Display Image"])

    small_img = scale_down(img)
    show_images([small_img], ["Small Image"])
    save_images([small_img], [str(output_path / "small.jpg")])

    blue, green, red = separate_channels(small_img)
    show_images([small_img, blue, green, red], ["Original", "Blue", "Green", "Red"])

    save_images(
        [blue, green, red],
        [str(output_path / f"{name}.png") for name in ["blue", "green", "red"]]
    )