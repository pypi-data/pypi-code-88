""" pytest module to hold tests for webstaterator/templateengine.py """

import os
import shutil

import pytest

from webstaterator.templateengine import TemplateEngine

def make_template(path, file, template):
    temp_path = os.path.join(path,file)
    with open(temp_path,'w') as temp_out:
        temp_out.write(template)
    return temp_path

def make_list_template(path, file, name):
    with open(os.path.join(path,file),'w') as temp_out:
        temp_out.write("{%for item in "+name+" %}{{ item }}{% endfor %}")

def make_dict_template(path, file, name):
    with open(os.path.join(path,file),'w') as temp_out:
        temp_out.write(
            "{%for k,v in "+name+".items() %}{{ k }}={{ v }}---{% endfor %}"
        )

@pytest.fixture()
def get_test_template_engine():
    path = os.path.join(os.getcwd(),'test_templates')

    if(os.path.exists(path)):
        shutil.rmtree(path)

    os.mkdir(path)

    make_template(path, "basic.html", "test")
    make_dict_template(path, "model.html", "model")
    make_list_template(path, "links.html","links")
    make_dict_template(path, "target.html", "target")

    yield TemplateEngine(path)
    shutil.rmtree(path)

def test_create_website_instance(get_test_template_engine):
    assert isinstance(get_test_template_engine,TemplateEngine)

def test_basic_template(get_test_template_engine):
    get_test_template_engine.model = {}
    get_test_template_engine.links = []
    result = get_test_template_engine.generate_page(
        template='basic.html',
        save_path = None,
        page_link = 'basic.html'
        )
    assert result == "test"

def test_links(get_test_template_engine):
    links = ['one.html','two.html']
    get_test_template_engine.model = {}
    get_test_template_engine.links = links
    result = get_test_template_engine.generate_page(
        template='links.html',
        save_path = None,
        page_link = "one.html"
        )
    assert result == "".join(links)

def test_basic_model(get_test_template_engine):

    model = {
        "a":1,
        "b":2,
        "c":3
    }

    model_flattened = ""
    for k,v in model.items():
        model_flattened += "{}={}---".format(k,v)

    get_test_template_engine.model = model
    get_test_template_engine.links = {}
    result = get_test_template_engine.generate_page(
        template='model.html',
        save_path = None,
        page_link = "model.html"
        )
    assert result == model_flattened

def test_page_link(get_test_template_engine):

    make_template(
        get_test_template_engine.template_path,
        "page_link.html",
        """{% for page,links in links.items() %}{% if page_link in links %}{{ page }}{% endif %}{% endfor %}"""
    )
    get_test_template_engine.model = {}
    get_test_template_engine.links = {
        "page1":["page1.html"],
        "page2":["page2.html"],
        "target":["target.html"]
    }
    result = get_test_template_engine.generate_page(
        template='page_link.html',
        target = None,
        save_path = None,
        page_link = "target.html"
        )
    assert result == "target"

def test_target(get_test_template_engine):
    target = {
        "ta":1,
        "tb":2,
        "tc":3
    }

    target_flattened = ""
    for k,v in target.items():
        target_flattened += "{}={}---".format(k,v)

    get_test_template_engine.model = {}
    get_test_template_engine.links = {}
    result = get_test_template_engine.generate_page(
        template='target.html',
        target = target,
        save_path = None,
        page_link = "target.html"
        )
    assert result == target_flattened

def test_saving_page(get_test_template_engine):
    page_link = "test_page.html"
    save_path = os.path.join(os.getcwd(),page_link)
    get_test_template_engine.model = {},
    get_test_template_engine.links = [],
    result = get_test_template_engine.generate_page(
        template='basic.html',
        save_path = save_path,
        page_link = page_link
        )

    assert result == "test"
    assert os.path.exists(save_path)

    with open(save_path,"r") as page_stream:
        assert page_stream.read() == "test"

    os.remove(save_path)

def test_has_template_success(get_test_template_engine):
    assert get_test_template_engine.has_template("model.html")

def test_has_template_fail(get_test_template_engine):
    assert not get_test_template_engine.has_template("no_template_found.html")
