import argparse
import os
import requests as req

def main():
    parser = argparse.ArgumentParser(prog ='flaskcli',
                                     description ='create flask app using cli')
    parser.add_argument("create-flask-app",help="create flask app with default filenames")
    parser.add_argument("-pyfn","-pyfilename",help="Flask python file name",default="app")
    args = parser.parse_args()
    pythonfilename = args.pyfn.split(".")[0]
    pythonfile = open(pythonfilename+".py","w")
    os.mkdir("templates")
    os.mkdir("static")
    basehtmltxt = req.get("https://raw.githubusercontent.com/logan0501/create-flask-project-cli/main/flask-files/base.html")
    indexhtmltxt = req.get("https://raw.githubusercontent.com/logan0501/create-flask-project-cli/main/flask-files/index.html")
    cssfiletxt = req.get("https://raw.githubusercontent.com/logan0501/create-flask-project-cli/main/flask-files/style.css")
    pythonfiletxt = req.get("https://raw.githubusercontent.com/logan0501/create-flask-project-cli/main/flask-files/app.py")
    indexhtmlfile = open("./templates/index.html","w")
    indexhtmlfile.write(indexhtmltxt.text)
    basehtmlfile = open("./templates/base.html","w")
    basehtmlfile.write(basehtmltxt.text)
    cssfile = open("./static/style.css","w")
    cssfile.write(cssfiletxt.text)
    pythonfile.write(pythonfiletxt.text)
    
    print('sucessfully created')
