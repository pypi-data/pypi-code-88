#!/usr/bin/env python
# coding:utf-8
"""
#set:usage,examples,changelog
##################################################################
# USAGE :
#s
import donotimport

#Your code is here without any import to any library
#e
##################################################################
# EXAMPLES :
#s

# Example:1
import donotimport

#For encryption
p1=ashar("123","Example:1").encode()
print(p1)
# OUTPUT:
'''
-If the library is already installed, the result will be:
25#;F7=04-62%12?11<F0[54{89(E5:00O15z1AbA6BABHA2r@204xC5H9Fx2FSCFt98X72)B0}65]BA>77!5F$D9&37_B3+001

-If the library is not installed, an error message will appear:
ashar not exist!
'''
#e
##################################################################
"""
# VALUES :
#s
__version__="0.0.1"
__name__="donotimport"
__author__="Yasser BDJ (Ro0t96)"
__author_email__="by.root96@gmail.com"
__github_user_name__="byRo0t96"
__title__="donotimport"
__description__="A simple package to prevent the abusive use of the import statement in Python."
__author_website__="https://byro0t96.github.io/"
__source_code__=f"https://github.com/{__github_user_name__}/{__name__}"
__keywords__=['python','donotimport']
__install_requires__=[]
__Installation__="pip install "+__name__+"=="+__version__
__license__='Apache Software License'
__license_text__=f'''Copyright (c) 2008->Present, {__author__}
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.'''
__copyright__='Copyright 2008 -> Present, '+__author__

__changelog__='## 0.0.1\n- First public release.\n'
##################################################################
#e

#s
import os
import sys

def rd(script_file):
    with open(script_file,'r') as file:
        data=file.read()
    exec(data)
pkgs=[]
errs=True
while errs==True:
    try:
        for i in range(len(pkgs)):
            try:
                exec(pkgs[i])
            except:
                pass
        os.system('cls' if os.name=='nt' else 'clear')
        rd(sys.argv[0])
        errs=False
    except Exception as err:
        err=str(err)
        if err[0:6]=="name '":
            try:
                exec('import '+err.split("'")[1])
            except:
                print("'"+err.split("'")[1]+"' not exist!")
                exit()
            pkgs.append('import '+err.split("'")[1])
        elif err=="'module' object is not callable":
            pkgs[i]='from '+pkgs[i].split(" ")[1]+' import '+pkgs[i].split(" ")[1]
        else:
            print(err)
            errs=False
exit()
#e