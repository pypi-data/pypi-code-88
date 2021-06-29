import compileall, os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
dirs =  [
	BASE_DIR +"\\django_microsip_base\\apps\\main",
	BASE_DIR +"\\django_microsip_base\\data",
	BASE_DIR +"\\django_microsip_base\\libs",
	BASE_DIR +"\\django_microsip_base\\settings",
	BASE_DIR +"\\django_microsip_base\\urls",
	BASE_DIR +"\\django_microsip_base\\con",
]

for directorio in dirs:
	compileall.compile_dir(directorio, force=True)
	
compileall.compile_file(BASE_DIR +"\\django_microsip_base\\context_processors.py")

