""" pytest module to hold tests for webstaterator/website.py """

import os
import json
import shutil

import pytest

from webstaterator.website import Website
from webstaterator.website import InvalidPagesException
from webstaterator.website import InvalidModelException
from webstaterator.website import InvalidWebsiteException
from webstaterator.website import PageAttributes

def test_create_website_instance():
    """ Check an instance of website can be created """
    assert isinstance(Website(),Website)

#--- test data generators ------------------------------------------------------
def create_page(name,template,filename):
    """ helper method to create a valid page """
    return {
            'name':name,
            'template':template,
            'filename':filename
        }

def create_multipage(name,template,model_list,model_id,filename):
    """ helper method to create a valid page """
    return {
            'name':name,
            'template':template,
            'list':model_list,
            'id':model_id,
            'filename':filename
        }

def get_valid_pages():
    """ helper method to create a valid list of pages """
    return [
            create_page('test1','index.html','index.html'),
            create_page('test2','links.html','items.html')
    ]

def get_duplicate_pages():
    """ helper method to create a list of pages containing duplicates """
    return [
            create_page('test1','index.html','index.html'),
            create_page('test2','links.html','items.html'),
            create_page('test1','index.html','index.html'),
    ]

def get_invalid_pages():
    """ helper method to create an invalid list of pages """
    return [
            create_page('test1','index.html','index.html'),
            {
                'name':'invalid',
                'template':'error.html'
            }
    ]

def get_valid_pages_with_lists():
    """ helper method that creates a list of pages including one multipage """

    return [
            create_page('test1','index.html','index.html'),
            create_page('test2','links.html','items.html'),
            create_multipage('test3','items.html','items','id','item-{}.html')
    ]

def get_basic_website(pages):
    return {
        'name':'test',
        'template':'templates',
        'pages':pages
    }

def get_website_with_model(pages,model):
    website = get_basic_website(pages)
    website['model'] = model
    return website

@pytest.fixture()
def get_test_website_model():
    website_dict = get_basic_website(get_valid_pages())
    website_path = os.path.join(os.getcwd(),'test_website.js')

    with open(website_path,'w') as website_stream:
        json.dump(website_dict,website_stream)

    yield website_dict, website_path

    os.remove(website_path)

@pytest.fixture()
def get_test_asset_folder():
    asset_path = os.path.join(os.getcwd(),"tests_assets")
    if(os.path.exists(asset_path)):
        shutil.rmtree(asset_path)

    os.mkdir(asset_path)
    yield asset_path
    shutil.rmtree(asset_path)

#--- load tests ----------------------------------------------------------------
def test_load_with_dict():
    test_website = Website()
    website_dict = get_basic_website(get_valid_pages())
    test_website.load(website_dict)

    assert isinstance(test_website,Website)
    assert test_website.name == website_dict['name']
    assert test_website.template_path == website_dict['template']
    assert test_website.pages == website_dict['pages']

def test_load_dict_with_bad_template():
    test_website = Website()

    website_with_bad_template_path = get_basic_website(get_valid_pages())
    website_with_bad_template_path['template'] = 'missing_folder'

    with pytest.raises(InvalidWebsiteException):
        test_website.load(website_with_bad_template_path)

def test_load_with_json_file(get_test_website_model):
    test_website = Website()
    website_dict = get_test_website_model[0]
    test_website.load(get_test_website_model[1])

    assert isinstance(test_website,Website)
    assert test_website.name == website_dict['name']
    assert test_website.template_path == website_dict['template']
    assert test_website.pages == website_dict['pages']

def test_load_with_json_string():
    test_website = Website()
    website_dict = get_basic_website(get_valid_pages())
    json_website = json.dumps(website_dict)
    test_website.load(json_website)

    assert isinstance(test_website,Website)
    assert test_website.name == website_dict['name']
    assert test_website.template_path == website_dict['template']
    assert test_website.pages == website_dict['pages']

def test_load_with_assets(get_test_asset_folder):
    test_website = Website()
    website_dict = get_basic_website(get_valid_pages())
    website_dict['assets'] = [get_test_asset_folder]
    test_website.load(website_dict)

    assert test_website.asset_paths == website_dict['assets']

def test_to_dict():
    test_website = Website()
    website_dict = get_basic_website(get_valid_pages())
    test_website.load(website_dict)

    website_obj = test_website.to_dict()

    assert website_obj['name'] == website_dict['name']
    assert website_obj['template'] == website_dict['template']
    assert website_obj['pages'] == website_dict['pages']

#--- model tests ---------------------------------------------------------------
def test_set_model_with_dict():
    """ Test that a model can be set as a dict """
    test_website = Website()
    assert test_website.model == {}

    test_model = {'a':1,'b':2,'c':3}
    test_website.model = test_model
    assert test_website.model == test_model

def test_set_model_with_json_string():
    """ test that a model can be set using a json string """
    test_website = Website()
    assert test_website.model == {}

    test_model = """{"a":1,"b":2,"c":3}"""
    test_website.model = test_model
    json_model = json.loads(test_model)
    assert test_website.model == json_model

def test_set_model_with_json_file():
    """ test that a model can be set using a json file """
    test_website = Website()
    assert test_website.model == {}

    test_model = """{"a":1,"b":2,"c":3}"""
    file_path = os.path.join(os.getcwd(),"test_model.json")
    with open(file_path,'w') as file_out:
        file_out.write(test_model)
    test_website.model = file_path
    os.remove(file_path)
    json_model = json.loads(test_model)

    assert test_website.model == json_model

#--- pages tests ---------------------------------------------------------------
def test_pages_validation_empty_list():
    """ test to check that setting pages to an empty list results in a raised
    exception """
    test_website = Website()
    with pytest.raises(InvalidPagesException):
        test_website.pages = []

def test_valid_pages():
    """ test to check that pages accepts a valid list of pages """
    test_website = Website()
    test_website.pages =get_valid_pages()
    assert test_website.pages == get_valid_pages()

def test_invalid_pages():
    """ test to check that setting pages to an invalid list of pages raises
    an exception """
    test_website = Website()
    with pytest.raises(InvalidPagesException):
        test_website.pages = get_invalid_pages()

def test_duplicate_pages():
    test_website = Website()
    with pytest.raises(InvalidPagesException):
        test_website.pages = get_duplicate_pages()

#--- link tests ----------------------------------------------------------------
def test_validate_list_page_with_valid_filename():
    page = create_multipage(
        'test',
        'tmp.html',
        'model',
        None,
        'out-{}.html'
    )
    assert Website.validate_list_page(page) == True


def test_validate_list_page_with_invalid_filename():
    page = create_multipage(
        'test',
        'tmp.html',
        'model',
        None,
        'out.html'
    )
    with pytest.raises(InvalidPagesException):
        Website.validate_list_page(page)


def test_get_target_model_with_valid_no_dot_target():
    target_obj = "test"
    obj = {
        "test":"value",
        "another":"value"
    }

    target = Website.get_target_model(target_obj, obj)
    assert target == obj[target_obj]


def test_get_target_model_with_valid_dot_target():
    target_obj = "missing"
    obj = {
        "test":"value",
        "another":"value"
    }

    with pytest.raises(InvalidModelException):
        target = Website.get_target_model(target_obj, obj)


def test_get_target_model_with_invalid_no_dot_target():
    target_obj = "test.nested.value"
    obj = {
        "test":{
            "nested":{
                "value":"hello",
                "value2":"world"
            }
        },
        "another":"value"
    }

    target = Website.get_target_model(target_obj, obj)
    assert target == obj["test"]["nested"]["value"]


@pytest.mark.parametrize('target_obj',[
    'test.nested.missing',
    'test.missing.value',
    'missing.nested.value',
    'test.nested.']
)
def test_get_target_model_with_invalid_dot_target(target_obj):
    obj = {
        "test":{
            "nested":{
                "value":"hello",
                "value2":"world"
            }
        },
        "another":"value"
    }

    with pytest.raises(InvalidModelException):
        target = Website.get_target_model(target_obj, obj)


def test_basic_link_generation():
    """Test single page link generation"""
    test_website = Website()
    pages = get_valid_pages()
    test_website.pages = pages
    test_website.model = """{"a":1,"b":2,"c":3}"""
    assert test_website.generate_links() is True
    expected_links = {p[PageAttributes.NAME]:[p[PageAttributes.FILENAME]] for p in pages}
    assert test_website.links == expected_links

def test_list_link_generation():
    """Test single page link generation"""
    test_website = Website()
    pages = get_valid_pages_with_lists()
    test_website.pages = pages
    test_website.model = """{"a":1,"b":2,"c":3,"items":[{"id":1},{"id":2}]}"""

    assert test_website.generate_links() is True

    expected_links = {
                "test1":["index.html"],
                "test2":["items.html"],
                "test3":["item-1.html","item-2.html"]
    }

    assert test_website.links == expected_links

def test_list_link_generation_with_dict():
    """Test single page link generation"""
    test_website = Website()
    pages = get_valid_pages_with_lists()
    test_website.pages = pages
    test_website.model = """{"a":1,"b":2,"c":3,"items":{"1":{"id":1},"2":{"id":2}}}"""

    assert test_website.generate_links() is True

    expected_links = {
                "test1":["index.html"],
                "test2":["items.html"],
                "test3":["item-1.html","item-2.html"]
    }

    assert test_website.links == expected_links

def test_list_link_target_model():
    """Test single page link generation"""
    test_website = Website()
    pages = get_valid_pages_with_lists()
    test_website.pages = pages
    test_website.model = """{"a":1,"b":2,"c":3,"items":[{"id":1},{"id":2}]}"""

    assert test_website.generate_links() is True

    expected_targets = {
                "index.html":None,
                "items.html":None,
                "item-1.html":{"id":1},
                "item-2.html":{"id":2}
    }

    for url, target in expected_targets.items():
        assert test_website.get_target(url) == target

def test_deep_list_link_generation():
    """Test multipage link generation"""
    test_website = Website()
    pages = get_valid_pages()
    pages.append(create_multipage("test3","item.html","items.foo.bar","id","item-{}.html"))
    test_website.pages = pages
    test_website.model = {
        "a":1,
        "b":2,
        "c":3,
        "items":{
            "foo":{
                "bar":[
                    {"id":"dog"},
                    {"id":"cat"},
                    {"id":"fish"},
                ]
            }
        }
    }

    assert test_website.generate_links() is True

    expected_links = {
                "test1":["index.html"],
                "test2":["items.html"],
                "test3":["item-dog.html","item-cat.html","item-fish.html"]
    }

    assert test_website.links == expected_links

def test_list_link_invalid_filename():
    """Test multipage invalid filename"""
    test_website = Website()
    pages = get_valid_pages()
    pages.append(create_multipage("test3","item.html","items","id","item.html"))
    test_website.pages = pages
    test_website.model = """{"a":1,"b":2,"c":3,"items":[{"id":1},{"id":2}]}"""

    with pytest.raises(InvalidPagesException):
        test_website.generate_links()

def test_list_link_missing_obj():
    """Test multipage model missing object"""
    test_website = Website()
    pages = get_valid_pages()
    pages.append(create_multipage("test3","item.html","items.foo.bar","id","item-{}.html"))
    test_website.pages = pages
    test_website.model = """{"a":1,"b":2,"c":3,"items":[{"id":1},{"id":2}]}"""

    with pytest.raises(InvalidModelException):
        test_website.generate_links()

def test_list_link_missing_id():
    """Test multipage model missing id"""
    test_website = Website()
    pages = get_valid_pages()
    pages.append(create_multipage("test3","item.html","items","foo","item-{}.html"))
    test_website.pages = pages
    test_website.model = """{"a":1,"b":2,"c":3,"items":[{"id":1},{"id":2}]}"""

    with pytest.raises(InvalidModelException):
        test_website.generate_links()

def test_list_link_missing_some_ids():
    """Test multipage model missing some ids"""
    test_website = Website()
    pages = get_valid_pages()
    pages.append(create_multipage("test3","item.html","items","id","item-{}.html"))
    test_website.pages = pages
    test_website.model = """{"a":1,"b":2,"c":3,"items":[{"id":1},{"foo":2}]}"""

    with pytest.raises(InvalidModelException):
        test_website.generate_links()
