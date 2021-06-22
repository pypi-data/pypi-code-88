"""
Webstaterator

A Python tool for generating static websites based on object models

Documentation: https://gitlab.com/Jon.Keatley.Folio/webstaterator
Gitlab: https://gitlab.com/Jon.Keatley.Folio/webstaterator
PyPi: https://pypi.org/project/webstaterator/

Created by Jon Keatley (http://jon-keatley.com)
Named by Sasha Siegel. It is her fault!

Copyright Jon Keatley 2021

"""

import sys
import os
import shutil
import json

from webstaterator.website import Website, PageAttributes
from webstaterator.templateengine import TemplateEngine

class Webstaterator:
    """ A Python tool for generating static websites based on object models """

    @staticmethod
    def validate(website_model):
        """ Validates a websites settings """
        website = Website()

        try:
            website.load(website_model)
            templates = TemplateEngine(website.template_path)

            #check all templates exist
            pages = website.pages
            missing_page_format = "Template {} for page {} was not found"

            has_error = False
            for page in pages:
                if not templates.has_template(page[PageAttributes.TEMPLATE]):
                    err = missing_page_format.format(
                        page[PageAttributes.TEMPLATE],
                        page[PageAttributes.NAME]
                    )
                    has_error = True
                    print(err)


            website.generate_links()

            if not has_error:
                print("Ok")
        except Exception as ex: # pylint: disable=W0703
            print("An error was found with your website!")
            print("Error: {}. Message: {}".format(type(ex).__name__,ex.args))


    @staticmethod
    def build(website_model, path):
        """ Builds a website based on the provided settings """

        # add check for path
        if os.path.isdir(path):
            shutil.rmtree(path)
        os.mkdir(path)

        print("Loading ...")
        website = Website()
        try:
            website.load(website_model)
            website.generate_links()
            templates = TemplateEngine(website.template_path)
            templates.model = website.model
            templates.links = website.links
        except Exception as ex: # pylint: disable=W0703
            print("An error was found with your website!")
            print("Error: {}. Message: {}".format(type(ex).__name__,ex.args))
            sys.exit(-1)

        links = website.links

        if website.asset_paths is not None:
            print("copying assets")
            for asset in website.asset_paths:
                if os.path.isdir(asset):
                    dir_name = os.path.basename(asset)
                    new_asset_path = os.path.join(path,dir_name)

                    shutil.copytree(
                        asset,
                        new_asset_path
                    )
                else:
                    print("Asset path {} does not exist".format(website.asset_paths))
                    sys.exit(-1)


        print("Building website")
        for page in website.pages:
            page_links = links[page[PageAttributes.NAME]]

            for page_link in page_links:
                save_path = os.path.join(path,page_link)
                templates.generate_page(
                    page[PageAttributes.TEMPLATE],
                    save_path,
                    page_link,
                    target = website.get_target(page_link)
                )

        print("Built!")


    @staticmethod
    def template(path):
        """ Generates a template for a website """

        print("Building template")
        # create target folder if it does not exist
        if os.path.isdir(path):
            shutil.rmtree(path)
        os.mkdir(path)

        temp_name = "templates"
        asset_name = "assets"
        os.mkdir(os.path.join(path,temp_name))
        os.mkdir(os.path.join(path,asset_name))

        model_name = "model.json"
        model_dict = {"example":"hello world"}
        with open(os.path.join(path, model_name), 'w') as model_out:
            json.dump(model_dict, model_out, indent=4)

        template_name = "template.html"
        with open(os.path.join(path, temp_name, template_name), 'w') as temp_out:
            temp_out.write("<html>\n\t<head>\n\t\t<title>Example</title>\n\t</head>")
            temp_out.write("\n\t<body>\n\t\t<h1>{{ model['example'] }}</h1>")
            temp_out.write("\n\t</body>\n</html>")

        website = Website()
        website.name = "insert name"
        website.template_path = temp_name
        website.asset_paths = [asset_name]
        website.pages = [{
                'name':'example',
                'template':template_name,
                'filename':'example.html'
            }]

        with open(os.path.join(path,"website.json"), 'w') as website_out:
            json.dump(website.to_dict(model_name), website_out, indent=4)

        print("Built")
