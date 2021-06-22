""" pytest module to hold tests for webstaterator/templateengine.py """

import os
import shutil
import datetime

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

def make_date_filter_template(path, file, name, in_format = None):
    with open(os.path.join(path,file),'w') as temp_out:
        if in_format is None:
            temp_out.write("{{ model['"+name+"']|date_fmt }}")
        else:
            temp_out.write('{{ model["'+name+'"]|date_fmt("%d %b %y","'+ in_format +'")}}')

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
    make_date_filter_template(path, "filter.html", "test_date")
    make_date_filter_template(path, "filter_cust.html", "test_date","%d-%m-%Y")

    yield TemplateEngine(path)
    shutil.rmtree(path)

def test_create_website_instance(get_test_template_engine):
    assert isinstance(get_test_template_engine,TemplateEngine)

def test_properties(tmpdir):
    engine = TemplateEngine(tmpdir)
    model = {"result":"success"}
    engine.model = model
    assert engine.model == model
    links = ["this.html"]
    engine.links = links
    assert engine.links == links

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

def test_date_filter_directly_with_date(get_test_template_engine):
    test_date = datetime.date(2021,1,1)
    test_date =  get_test_template_engine._date_filter(test_date)
    assert test_date == "01 Jan 21"

def test_date_filter_directly_with_datetime(get_test_template_engine):
    test_date = datetime.datetime(2021,2,2,1,0,0,0)
    test_date =  get_test_template_engine._date_filter(test_date)
    assert test_date == "02 Feb 21"

def test_date_filter_directly_with_str(get_test_template_engine):
    test_date = get_test_template_engine._date_filter("2021-03-03")
    assert test_date == "03 Mar 21"

def test_date_filter_in_template(get_test_template_engine):
    get_test_template_engine.model = {"test_date":"2021-04-04"}
    get_test_template_engine.links = []
    result = get_test_template_engine.generate_page(
        template="filter.html",
        save_path = None,
        page_link = "filter.html"
        )
    assert result == "04 Apr 21"

def test_date_filter_in_template_with_custom_input_format(get_test_template_engine):
    get_test_template_engine.model = {"test_date":"04-04-2021"}
    get_test_template_engine.links = []
    result = get_test_template_engine.generate_page(
        template="filter_cust.html",
        save_path = None,
        page_link = "filter_cust.html"
        )
    assert result == "04 Apr 21"
