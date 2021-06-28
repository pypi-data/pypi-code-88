from ..structure import Readme,Section
from ..elements import Element
from typing import Union

def generate(readme_obj: Readme, type: str='md', file_name:str="README.md"):
    inner_data:str = ""
    
    if type == 'md':
        inner_data = readme_obj.to_markdown()
    
    with open(file_name,"w") as f:
        f.write(inner_data)

def md(element:Union[Element,Section]):
    return element.to_markdown()