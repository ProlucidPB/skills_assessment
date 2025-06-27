import sys
from utils import convert_to_ascii


def main():
    if len(sys.argv) < 2:
        print("Usage: ascii_art.py <image_path> [width]")
        sys.exit(1)

    image_path = sys.argv[1]
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 80

    art = convert_to_ascii(image_path, width)
    print(art)

if __name__ == "__main__":
    main()