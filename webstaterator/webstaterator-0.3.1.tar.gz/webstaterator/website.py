"""
Holds all the details for a website
"""

import os
import json
from collections.abc import Mapping

class InvalidPagesException(Exception):
    """ Exception used to indecate an invalid page object. Raised by Website """
    def __init__(self,msg,error = "Page model invalid"):
        self.error = error
        super().__init__(msg)

class InvalidModelException(Exception):
    """ Exception used to indecate an invalid data object. Raised by Website """
    def __init__(self,msg,error = "Data model invalid"):
        self.error = error
        super().__init__(msg)

class InvalidWebsiteException(Exception):
    """ Exception used to indecate an invalid website object. Raised by Website """
    def __init__(self,msg,error = "Website model invalid"):
        self.error = error
        super().__init__(msg)

class WebsiteAttributes:
    # pylint: disable=R0903
    # Too few public methods - Didn't find a nicer way to do this
    """ Holds string values for all website attributes """
    NAME = 'name'
    MODEL = 'model'
    TEMPLATE = 'template'
    ASSETS = 'assets'
    PAGES = 'pages'

    OPTIONAL_ATTRIBUTES = [
        ASSETS,
        MODEL
    ]

    REQUIRED_ATTRIBUTES = [
        NAME,
        TEMPLATE,
        PAGES
    ]

class PageAttributes:
    # pylint: disable=R0903
    # Too few public methods - Didn't find a nicer way to do this
    """ Holds string values for all page attributes """
    LIST = 'list'
    ID = 'id'
    NAME ='name'
    TEMPLATE = 'template'
    FILENAME = 'filename'

    OPTIONAL_ATTRIBUTES = [
        LIST,
        ID,
    ]
    REQUIRED_ATTRIBUTES = [
        NAME,
        TEMPLATE,
        FILENAME,
    ]

MODEL_ERR_FMT = "'{}' missing from model '{}'"
PAGE_ERR_FMT = "multipages must contain a '{{}}' in their {}"

class Website: # pylint: disable=R0902
    """ Represents a Website, holds detail on the pages to generated
        and the data model to use during generation
    """

    def __init__(self):
        """ Website represents the various aspects of the website """
        self._name = None
        self._template_path = None
        self._asset_paths = None
        self._links = {}
        self._targets = {}
        self._has_generated_links = False
        self._model = {}
        self._pages = []

#--- load ----------------------------------------------------------------------
    @staticmethod
    def __process_path(target_path):
        """ Checks target_path exists and handles relative and user paths """
        if '~' in target_path:
            target_path = os.path.expanduser(target_path)

        if target_path.endswith(os.path.sep):
            target_path = target_path[:-1]

        if not os.path.isdir(target_path):
            target_path = os.path.join(os.getcwd(),target_path)
            if not os.path.isdir(target_path):
                err_str = "Template folder {} not found".format(target_path)
                raise InvalidWebsiteException(err_str)
        return target_path

    def load(self,website):
        """ Load in a website either from json string, a dictionary, or a file path """
        self._has_generated_links = False
        website_obj = {}
        if isinstance(website, Mapping):
            website_obj = website
        else:
            website_obj = Website.__set_json_from_str_or_file(website)
            if os.path.isfile(website) and len(os.path.dirname(website)) > 0:
                #print(f"changing dir to {os.path.dirname(website)}" )
                os.chdir(os.path.dirname(website))

        Website.__validate_website(website_obj)

        self._template_path = Website.__process_path(
            website_obj[WebsiteAttributes.TEMPLATE]
        )

        self._name = website_obj[WebsiteAttributes.NAME]
        self._pages = website_obj[WebsiteAttributes.PAGES]

        if WebsiteAttributes.MODEL in website_obj:
            self.model = website_obj[WebsiteAttributes.MODEL]

        if WebsiteAttributes.ASSETS in website_obj:
            assets = website_obj[WebsiteAttributes.ASSETS]

            self._asset_paths = [
                Website.__process_path(asset)
                for asset in assets
            ]

    @staticmethod
    def __validate_website(website):
        """ Inspects website dictionary to check it has all required attributes """
        for required_attr in WebsiteAttributes.REQUIRED_ATTRIBUTES:
            if required_attr not in website:
                err_str = "website is missing {}".format(required_attr)
                raise InvalidWebsiteException(err_str)

        if Website.__validate_pages(website[WebsiteAttributes.PAGES]):
            return True
        return False

#--- basic properties ----------------------------------------------------------
    @property
    def name(self):
        """ get for name """
        return self._name

    @name.setter
    def name(self, value):
        """ set name """
        self._name = value

    @property
    def template_path(self):
        """ get for template_path """
        return self._template_path

    @template_path.setter
    def template_path(self, value):
        """ set template_path """
        self._template_path = value

    @property
    def asset_paths(self):
        """ get for asset paths """
        return self._asset_paths

    @asset_paths.setter
    def asset_paths(self, value):
        """ set for asset_paths
            :value: List of asset paths
        """
        self._asset_paths = value

#--- model ---------------------------------------------------------------------
    @property
    def model(self):
        """ get for model """
        return self._model

    @model.setter
    def model(self, value):
        """ set for model. Clears links
            :value: Either a dict, a json string, or a json file
        """
        self._has_generated_links = False
        if isinstance(value, Mapping):
            self._model = value
        else:
            self._model = Website.__set_json_from_str_or_file(value)

#--- pages ---------------------------------------------------------------------

    @property
    def pages(self):
        """ get pages """
        return self._pages

    @pages.setter
    def pages(self,value):
        """ set pages. Clears links
            :value: Either a dict, a json string or a json file
        """
        new_pages = []
        self._has_generated_links = False
        if isinstance(value,list): #we need to rethink this
            new_pages = value
        else:
            new_pages = Website.__set_json_from_str_or_file(value)

        if Website.__validate_pages(new_pages):
            self._pages = new_pages

    @staticmethod
    def __validate_pages(pages):
        """ Validate pages model
            :returns: True if valid
            :rases: InvalidPagesException if invalid
        """

        if len(pages) == 0:
            raise InvalidPagesException("No pages found!")

        if not isinstance(pages,list):
            err_str = "Expected list of pages, found {}".format(type(pages))
            raise InvalidPagesException(err_str)

        page_names = []

        for page in pages:
            for required_attr in PageAttributes.REQUIRED_ATTRIBUTES:
                if required_attr not in page:
                    page_name = "???"
                    if 'name' in page:
                        page_name = page['name']
                    err_str = "Required field '{}' is missing from the page called {}."
                    raise InvalidPagesException(err_str.format(required_attr,page_name))
            if page['name'] in page_names:
                err_str = "Page names must be unique. The name {} is used multiple times"
                raise InvalidPagesException(err_str.format(page['name']))

            page_names.append(page['name'])

        return True

#--- helpers -------------------------------------------------------------------
    @staticmethod
    def __set_json_from_str_or_file(value):
        obj = {}
        if os.path.isfile(value):
            with open(value,'r') as obj_in:
                obj = json.load(obj_in)
        else:
            obj = json.loads(value)
        return obj

    def to_dict(self, model_value = "model"):
        """ converts the website object to a dictionary """
        web_obj = {}
        web_obj[WebsiteAttributes.NAME] = self._name
        web_obj[WebsiteAttributes.MODEL] = model_value
        web_obj[WebsiteAttributes.TEMPLATE] = self._template_path
        web_obj[WebsiteAttributes.ASSETS] = self._asset_paths
        web_obj[WebsiteAttributes.PAGES] = self._pages

        return web_obj

#--- links ---------------------------------------------------------------------
    @staticmethod
    def validate_list_page(page):
        """ checks a list page object has all required elements"""
        if '{}' not in page[PageAttributes.FILENAME]:
            err_str = PAGE_ERR_FMT.format(PageAttributes.FILENAME)
            raise InvalidPagesException(err_str)
        return True

    @staticmethod
    def get_target_model(target_obj, obj):
        """ finds the target element within a dict """
        if '.' in target_obj:
            nestedmodel_obj = target_obj.split('.')
            breadcrumb = ""
            for obj_target in nestedmodel_obj:
                if obj_target not in obj:
                    err_str = MODEL_ERR_FMT.format(obj_target, breadcrumb[0:-1])
                    raise InvalidModelException(err_str)
                obj = obj[obj_target]
        else:
            if target_obj not in obj:
                err_str = MODEL_ERR_FMT.format(target_obj,'model')
                raise InvalidModelException(err_str)

            obj = obj[target_obj]
        return obj

    def generate_links(self):
        """ Generates based on a combination of model and pages """
        self._has_generated_links = False
        self._links.clear()
        self._targets.clear()

        err_str = ""

        for page in self._pages:
            if PageAttributes.LIST not in page:
                self._links[page[PageAttributes.NAME]] = [page[PageAttributes.FILENAME]]
                continue

            self.validate_list_page(page)
            model_obj = page[PageAttributes.LIST]

            obj = self.get_target_model(model_obj, self._model)

            item_links = []
            if isinstance(obj, Mapping):
                for key, item_obj in obj.items():
                    url = page[PageAttributes.FILENAME].format(key)
                    item_links.append(url)
                    self._targets[url] = item_obj
            else:
                if PageAttributes.ID not in page:
                    err_str = "Pages using the list attribute must include "
                    err_str+= "an id attribute or target a dictionary"
                    raise InvalidPagesException(err_str)
                model_id  = page[PageAttributes.ID]

                index = 0
                for item_obj in obj:
                    if model_id not in item_obj:
                        err_str = "{} at index {} is missing {}"
                        err_str = err_str.format(model_obj, index, model_id)
                        raise InvalidModelException(err_str)

                    url = page[PageAttributes.FILENAME].format(item_obj[model_id])
                    item_links.append(url)
                    self._targets[url] = item_obj
                    index += 1

            self._links[page[PageAttributes.NAME]] = item_links


        self._has_generated_links = len(self._links) > 0
        return self._has_generated_links

    @property
    def links(self):
        """ getter for _links """
        return self._links

    def get_target(self,link):
        """ returns the target for a given link or none """
        return self._targets.get(link, None)
