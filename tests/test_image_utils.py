import pytest
from image_utils import convert_to_ascii

def test_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        convert_to_ascii("no_such_file.png", 50)

def test_convert_small_image(tmp_path):
    # Create a 2×2 white image
    from PIL import Image
    img = Image.new("RGB", (2, 2), color="white")
    path = tmp_path / "white.png"
    img.save(path)

    art = convert_to_ascii(str(path), width=2)
    # all pixels white → lightest char (last in ASCII_CHARS)
    lines = art.splitlines()
    assert len(lines) == 2
    assert all(c == ASCII_CHARS[-1] for row in lines for c in row)