import os

def write_to_template(name_of_file):
    with open('index.html', 'r') as f:
        a = str(f.read())
        with open(f'''templates/{name_of_file}''', 'w') as t:
            t.write(a)
    os.remove('index.html')
    try:
        write_to_template('style.css')
    except FileNotFoundError:
        pass