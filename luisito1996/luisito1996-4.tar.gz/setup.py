from distutils.core import setup
import os
f = open ('/home/bravo/Escritorio/Prueba/requirements.txt','r')
requerimientos=[]
for linea in f:
	requerimientos.append(linea) 
f.close()
setup(
  name = 'luisito1996',
  packages = ['src'], # this must be the same as the name above
  version = '4',
  description = 'my description',
  author = 'Luis bravo',
  author_email = 'luisbravocollado@gmail.com',
  keywords = ['testing', 'logging', 'example'],
  classifiers = [],
  install_requires=requerimientos
)
