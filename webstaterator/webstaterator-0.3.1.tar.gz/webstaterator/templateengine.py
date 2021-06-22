"""
Responsible for managing the templating system and generating pages
"""

import datetime

from jinja2 import FileSystemLoader
from jinja2 import Environment
from jinja2.exceptions import TemplateNotFound

class TemplateEngine():
    """Provides a wrapper for the templating engine"""
    def __init__(self,template_path):
        self.env = Environment(
            loader = FileSystemLoader(template_path),
            autoescape = True
        )
        self.env.filters["date_fmt"] = TemplateEngine._date_filter

        self._template_path = template_path
        self._model = {}
        self._links = {}

    @staticmethod
    def _date_filter(
        date_in,
        date_format="%d %b %y",
        date_in_format="%Y-%m-%d"):
        """ Formats dates """
        if isinstance(date_in, str):
            date_in = datetime.datetime.strptime(date_in, date_in_format)

        return date_in.strftime(date_format)


    @property
    def template_path(self):
        """ get template_path """
        return self._template_path

    @property
    def model(self):
        """ get model """
        return self._model

    @model.setter
    def model(self,value):
        """ sets model """
        self._model = value

    @property
    def links(self):
        """ get links """
        return self._links

    @links.setter
    def links(self,value):
        """ sets links """
        self._links = value

    def generate_page(self, template, save_path, page_link, target = None):
        """Uses templating engine to generate a new page and saves it to save_path"""
        template = self.env.get_template(template)

        page = template.render(
            model = self._model,
            links = self._links,
            page_link = page_link,
            target = target,
        )

        if save_path is not None:
            with open(save_path,'w') as page_out:
                page_out.write(page)
            return page

        return page

    def has_template(self, template):
        """Checks to see if a template exists - returns True/False"""
        try:
            template = self.env.get_template(template)
            return template is not None
        except TemplateNotFound:
            return False
