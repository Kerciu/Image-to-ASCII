# TODO SCALE THE IMAGE
# TODO TRANSFORM TO THE SHADES OF GREY
# TODO MAP PIXELS TO ASCII
# TODO RENDER TEXT FILE

import os, sys
from PIL import Image
from dataclasses import dataclass


@dataclass
class Converter:

    @staticmethod
    def openImage(fileHandle: str) -> Image:
        try:
            with Image.open(fileHandle) as im:    
                return im

        except FileNotFoundError:
            raise FileNotFoundError("File was not found")
        except Exception as e:
            raise Exception("There was an error while processing your image: ", e)

    @staticmethod
    def scaleImage(image: Image, newWidth: int, newHeight: int) -> Image:
        try:
            if newWidth <= 0:
                newWidth = 1
            if newHeight <= 0:
                newHeight = 1

            scaled = image.resize((newWidth, newHeight))
            return scaled
        except Exception as e:
            raise Exception("There was an error while processing your image: ", e)
