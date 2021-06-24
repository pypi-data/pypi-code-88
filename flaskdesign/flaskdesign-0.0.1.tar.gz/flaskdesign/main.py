# -*- coding: utf-8 -*-

import os, sys

class ProjectDesing():
    def __init__(self, *args):
        ...
    
    def create_project(self, project_name):
        try:
            
            os.mkdir(project_name)
            
            module_file = open(os.path.join(project_name + os.path.sep + 
                               "__init__.py"), "w")
            
            main_file = open(os.path.join(project_name + os.path.sep + 
                             "app.py"), "w")
            
            content_main_file = ("# -*- coding: utf-8 -*-\n\n"
                                 "from flask import Flask\n\n"
                                 "app = Flask(__name__)\n\n")
            
            main_file.write(content_main_file)
            
            wsgi_file = open(os.path.join(project_name + os.path.sep + 
                             "wsgi.py"), "w")
            
            content_wsgi_file = ("#-*- coding: utf-8 -*-\n\n"
                                 "from app import app\n\n"
                                 "if __name__ == ('__main__'):\n"
                                 "    app.run(debug=True, port=5000)\n")
            
            wsgi_file.write(content_wsgi_file)
                                
        except Exception as error:
            print("Error: ", error)
    
    def create_app(self, app_name):
        try:
            os.mkdir(app_name)
            os.mkdir(os.path.join(app_name + os.path.sep + "templates"))
            os.mkdir(os.path.join(app_name + os.path.sep + "static"))
            os.mkdir(os.path.join(
                app_name + os.path.sep + "static" + os.path.sep + "js"))
            os.mkdir(os.path.join(
                app_name + os.path.sep + "static" + os.path.sep + "css"))
            os.mkdir(os.path.join(
                app_name + os.path.sep + "static" + os.path.sep + "img"))
            
            
            module_file = open(os.path.join(app_name + os.path.sep + 
                               "__init__.py"), "w")
            
            base_html_file = open(os.path.join(app_name + os.path.sep + 
                                  "templates" + os.path.sep + "base.html"), "w")
            
            models_file = open(os.path.join(app_name + os.path.sep + 
                               "models.py"), "w")
            
            models_file.write("#-*- coding: utf-8 -*-\n\n")
            
            controllers_file = open(os.path.join(app_name + os.path.sep + 
                                    "controllers.py"), "w")
            
            controllers_file.write("#-*- coding: utf-8 -*-\n\n"
                                   f"class {app_name.capitalize() + 'Controllers'}(object):\n"
                                   "    def __init__(self, *args):\n"
                                   "        ...\n")
            
            views_file = open(os.path.join(app_name + os.path.sep + 
                              "views.py"), "w")
            
            views_file.write("#-*- coding: utf-8 -*-\n\n"
                             "import os\n"
                             f"from {app_name}.controllers import {app_name.capitalize() + 'Controllers'}\n"
                             "from flask import Blueprint\n\n"
                             f"{app_name} = Blueprint('{app_name}', "
                             "__name__, template_folder='templates', "
                             "static_url_path=os.path.sep + "
                             f"'{app_name}' + os.path.sep + 'static', "
                             "static_folder='static')\n\n"
                             f"class {app_name.capitalize() + 'Views'}(object):\n"
                             "    def __init__(self, *args):\n"
                             "        ...\n")
                              
        except Exception as error:
            print("Error: ", error)
        
if __name__ == "__main__":
    try:
        args = sys.argv
        options = ["create_project", "create_app"]
        
        if args[1] not in options:
            print("Option is invalid!\nTry options: ", options)
        
        elif args[1] == "create_project":
            name_project = input("Input at name project: ")
            if name_project:
                ProjectDesing().create_project(name_project)
        
        elif args[1] == "create_app":
            name_app = input("Input at name app: ")
            if name_app:
                ProjectDesing().create_app(name_app)
    
    except Exception as error:
        print("Option is invalid!\nTry options: ", options)
        print("Error: ", error)
