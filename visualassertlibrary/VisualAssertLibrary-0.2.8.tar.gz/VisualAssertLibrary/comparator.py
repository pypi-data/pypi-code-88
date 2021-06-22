import os
from PIL import Image, ImageDraw
from robot.libraries.BuiltIn import BuiltIn
from .artifacts import Artifacts
from .config import *


class Comparator:
    """
    Compares screenshots to find differences.
    """
    def _region_analyze(self, image, x, y, width, height, factor):
        """
        Analyzes regions of the screenshot
        :param image: image of screenshot
        :param x, y, width, height: coordinates and size of the region to by analyzed
        :param factor: empirical parameter that determines the accuracy of the comparison
        :return:
        """
        region_status = 0
        for x_cord in range(x, x + width):
            for y_cord in range(y, y + height):
                try:
                    pixel = image.getpixel((x_cord, y_cord))
                    region_status += int(sum(pixel) / 3)
                except BaseException:
                    return None
        return region_status // factor

    def _analyze(self, image_actual, image_expected, cols, rows, factor):
        """
        Analyzes two images (actual result and expected result).
        It saves and returns abs path to joined screenshot (actual result/expected result/diff) if images differs.
        None returns if images are identical with a given accuracy.
        :param image_actual: abs path to screenshot with actual result.
        :param image_expected: abs path to screenshot with expected result.
        :param cols: qty of columns to split images
        :param rows: qty of rows to split images
        :return: None if images are identical, abs path to the saved file (actual/expected/diff) otherwise.
        """
        actual = Image.open(image_actual)
        expected = Image.open(image_expected)

        width, height = actual.size
        block_width = width // int(cols)
        block_height = height // int(rows)

        has_diff = False

        for x in range(0, width, block_width + 1):
            for y in range(0, height, block_height + 1):
                region_actual = self._region_analyze(
                    actual, x, y, block_width, block_height, factor)
                region_expected = self._region_analyze(
                    expected, x, y, block_width, block_height, factor)

                if region_actual != region_expected:
                    has_diff = True
                    draw = ImageDraw.Draw(actual)
                    draw.rectangle(
                        (x - 1, y - 1, x + block_width, y + block_height), outline="red")

        if has_diff:
            image_diff = os.path.join(
                os.path.split(image_actual)[0], f"diff-{os.path.split(image_actual)[1]}")

            actual.save(image_diff)
            joined_actual_expected_diff_path = Artifacts()._join_screenshots(
                image_actual, image_expected, image_diff)

            return joined_actual_expected_diff_path
        else:
            BuiltIn().log_to_console(
                "Images are identical on: FACTOR {f}, COLS {c}, ROWS {r}".format(f=factor, c=cols, r=rows))

            return None
