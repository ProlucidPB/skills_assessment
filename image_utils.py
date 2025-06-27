from PIL import Image
import numpy as np

ASCII_CHARS = "@%#*+=-:.  "

def convert_to_ascii(image_path: str, width: int) -> str:
    """
    TODO: implement this!
    - Open image at image_path
    - Resize to `width`, keeping aspect ratio
    - Convert to grayscale
    - Map each pixel to one of ASCII_CHARS (0→darkest, 255→lightest)
    - Return a string with newline separators
    - If file not found, raise FileNotFoundError
    """
    def load_image(image_path: str) -> Image.Image:
        """
        Load an image from the given path.
        Raises FileNotFoundError if the image does not exist.
        Returns a PIL Image object.
        """
        raise NotImplementedError("load_image not implemented")


    def resize_image(image: Image.Image, new_width: int) -> Image.Image:
        """
        Resize the image preserving aspect ratio based on new_width.
        Returns the resized PIL Image object.
        """
        raise NotImplementedError("resize_image not implemented")


    def grayify(image: Image.Image) -> Image.Image:
        """
        Convert the given PIL Image to grayscale.
        Returns the grayscale Image.
        """
        raise NotImplementedError("grayify not implemented")


    def pixels_to_ascii(image: Image.Image) -> str:
        """
        Map each pixel in the grayscale image to an ASCII char in ASCII_CHARS.
        Returns a string of ASCII characters representing the image.
        """
        raise NotImplementedError("convert_pixels_to_asciito_ascii not implemented")

    image = load_image(image_path)
    resized_image = resize_image(image)
    grayscale_image = grayify(resized_image)
    return pixels_to_ascii(grayscale_image)