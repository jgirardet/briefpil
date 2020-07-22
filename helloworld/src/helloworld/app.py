"""
My first application
"""
from pathlib import Path


def main():
    # This should start and launch your app!
    from PIL import Image
    a = Image.open(Path(__file__) / "../resources/helloworld.png")
    a.show()
