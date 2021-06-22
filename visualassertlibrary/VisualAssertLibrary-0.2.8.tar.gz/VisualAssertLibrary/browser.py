import os
from PIL import Image, ImageDraw
from robot.libraries.BuiltIn import BuiltIn
from .config import *


class Browser:
    """
    Works with a browser through selenium.
    """
    def _get_current_browser(self):
        """
        Gets current instance of the browser opened by SeleniumLibrary in a test.
        :return: instance of the browser
        """
        if hasattr(BuiltIn().get_library_instance(
                'SeleniumLibrary'), 'driver'):
            return BuiltIn().get_library_instance('SeleniumLibrary').driver
        else:
            return BuiltIn().get_library_instance('SeleniumLibrary')._current_browser()

    def _get_element_coordinates(self, element_locator):
        """
        Gets page location and size of the element.
        :param element_locator: XPATH locator to the element
        :return: element location on the page, element size
        """
        elements_coordinates_list = []
        browser = self._get_current_browser()
        elements = browser.find_elements_by_xpath(element_locator)
        for element in elements:
            location = element.location
            size = element.size
            elements_coordinates_list.append((location, size))

        return elements_coordinates_list

    def _exclude_elements(self, locator=None, screenshot=None, exclude=None):
        """
        Excludes elements from screenshot
        :param locator: string of XPATH locator to the element
        :param screenshot: abs path to the screenshot file
        :param exclude: string of XPATH locator to the element,
                        or list of XPATH locators to be excluded from screenshot
        :return: abs path to the screenshot with excluded elements
        """
        if exclude:
            if isinstance(exclude, str):
                exclude = [exclude, ]

        with Image.open(screenshot) as image:
            if locator:
                element_location, element_size = self._get_element_coordinates(locator)[0]
            else:
                element_location = {'x': 0, 'y': 0}

            for item in exclude:
                # excluded_element_location, excluded_element_size = self._get_element_coordinates(item)
                excluded_elements_coordinates_list = self._get_element_coordinates(item)
                for i in excluded_elements_coordinates_list:
                    excluded_element_location = i[0]
                    excluded_element_size = i[1]
                    x1 = excluded_element_location['x'] - element_location['x']
                    y1 = excluded_element_location['y'] - element_location['y']
                    x2 = x1 + excluded_element_size['width']
                    y2 = y1 + excluded_element_size['height']
                    draw = ImageDraw.Draw(image)
                    draw.rectangle([(x1, y1), (x2, y2)], fill="lightgrey")
            image.save(screenshot)

    def _save_screenshot(self, temp_dir=None, locator=None, name=None,
                         exclude=None, trim=None):
        """
        Saves screenshot to the temp dir.
        Captures the web element on the page matching to the passed locator,
        or the visible part of the page if locator is None
        :param temp_dir: abs path to the temp dir.
        :param locator: XPATH locator to the element on the page for screenshot
        :param name: name of the screenshot file
        :param exclude: string of XPATH locator to the element,
                                  or list of XPATH locators to be excluded from screenshot
        :param trim: number of pixels to trim screenshot
        :return: abs path to saved screenshot
        """
        browser = self._get_current_browser()
        screenshot_path = os.path.join(temp_dir, name)

        if locator:
            element = browser.find_element_by_xpath(locator)
            saved_screenshot = element.screenshot(screenshot_path)
        else:
            saved_screenshot = browser.get_screenshot_as_file(screenshot_path)

        if not saved_screenshot:
            raise Exception('Failed to save screenshot')

        if exclude:
            self._exclude_elements(locator, screenshot_path, exclude)

        if trim:
            im = Image.open(screenshot_path)
            width, height = im.size
            cropped_image = im.crop(
                (0 + int(trim),
                 0 + int(trim),
                    width - int(trim),
                    height - int(trim)))
            cropped_image.save(screenshot_path)

        return screenshot_path
