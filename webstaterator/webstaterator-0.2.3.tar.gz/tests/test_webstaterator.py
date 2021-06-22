""" pytest module to hold tests for webstaterator/__init__.py """

import os
import shutil

import pytest

from webstaterator.webstaterator import Webstaterator

from .test_website import get_basic_website
from .test_website import get_valid_pages
from .test_website import get_invalid_pages
from .test_website import get_valid_pages_with_lists
from .test_website import create_page
from .test_templateengine import make_template

#--- validator tests -----------------------------------------------------------
def create_path(tmpdir, name):
    new_path = os.path.join(str(tmpdir),name)

    if os.path.isdir(new_path):
        shutil.rmtree(new_path)

    os.mkdir(new_path)
    return new_path

def build_dummy_website(tmpdir, website, template_values = {}):
    path = os.path.join(tmpdir,website["template"])

    for page in website["pages"]:
        value = "test_template"
        if page["template"] in template_values:
            value = template_values[page["template"]]

        make_template(path, page["template"], value)

def assert_expected_files(build_path,expected_files):
    files = os.listdir(build_path)

    for file in expected_files:
        assert file in files


def test_validator_with_good_website(capsys, tmpdir):
    test_website = get_basic_website(get_valid_pages())
    test_website["template"] = str(tmpdir)
    build_dummy_website(tmpdir, test_website)

    weberator = Webstaterator()
    weberator.validate(test_website)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Ok'

def test_validator_with_good_website_with_assets(capsys, tmpdir):
    test_website = get_basic_website(get_valid_pages())
    test_website["template"] = str(tmpdir)
    test_website["assets"] = [str(tmpdir)]
    build_dummy_website(tmpdir, test_website)

    weberator = Webstaterator()
    weberator.validate(test_website)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Ok'

def test_validator_with_missing_templates(capsys):
    test_website = get_basic_website(get_valid_pages())

    weberator = Webstaterator()
    weberator.validate(test_website)
    captured = capsys.readouterr()
    assert captured.out.strip() != 'Ok'

def test_validator_with_missing_assets(capsys):
    test_website = get_basic_website(get_valid_pages())
    test_website["assets"] = "missing"

    weberator = Webstaterator()
    weberator.validate(test_website)
    captured = capsys.readouterr()
    assert captured.out.strip() != 'Ok'

def test_validator_with_bad_website_invalid_pages(capsys):

    weberator = Webstaterator()
    weberator.validate(get_basic_website(get_invalid_pages()))
    captured = capsys.readouterr()
    assert captured.out.strip() != 'Ok'

#--- build tests ---------------------------------------------------------------
def test_build_basic_website(capsys, tmpdir):
    build_path = create_path(tmpdir,"build")
    input_path =  create_path(tmpdir,"input")

    test_pages = get_valid_pages()

    test_website = get_basic_website(test_pages)
    test_website["template"] = input_path
    build_dummy_website(tmpdir, test_website)

    weberator = Webstaterator()

    weberator.build(test_website, build_path)

    for page in test_pages:
        assert os.path.exists(os.path.join(build_path,page["filename"]))

# test asset/
# test asset1 & 2
@pytest.mark.parametrize('assets',[
    (1, ['assets']),
    (2, ['assets_sep/']),
    (3, ['asset1','asset2'])]
)
def test_build_with_assets(tmpdir,assets):

    build_path =  create_path(tmpdir,f"build-{assets[0]}")
    input_path = create_path(tmpdir,"input")

    assets = assets[1]

    test_asset_format = "test-{}.css"

    asset_index = 1
    asset_paths = []
    for asset in assets:
        asset_paths.append(create_path(tmpdir,asset))

        asset_name = test_asset_format.format(asset_index)
        test_asset = os.path.join(asset_paths[-1],asset_name)
        with open(test_asset,"w") as asset_out:
            asset_out.write("BODY{background-color:#FF00FF;}")
        asset_index += 1

    test_website = get_basic_website(get_valid_pages())
    test_website["template"] = input_path
    test_website["assets"] = asset_paths
    build_dummy_website(tmpdir, test_website)

    weberator = Webstaterator()

    weberator.build(test_website, build_path)

    asset_index = 1
    for asset in assets:
        assert os.path.exists(os.path.join(build_path,asset)) == True
        assert os.path.exists(os.path.join(build_path,asset,test_asset_format.format(asset_index))) == True
        asset_index += 1


def test_build_model_access(tmpdir):
    build_path =  create_path(tmpdir,"build")
    input_path =  create_path(tmpdir,"input")
    item_template = """{% for item in model["values"] %}{{ item["name"] }}-{% endfor %}"""
    item_details = { "index.html": item_template }

    test_website = get_basic_website([create_page("index","index.html","index.html")])
    test_website["template"] = input_path
    model = {"values":[
        {"id":1, "name":"foo"},
        {"id":2, "name":"bar"},
        {"id":3, "name":"barfoo"}
    ]}
    test_website["model"] = model
    build_dummy_website(tmpdir, test_website, item_details)
    weberator = Webstaterator()
    weberator.build(test_website, build_path)

    assert_expected_files(build_path,["index.html"])

    test_page_path = os.path.join(build_path,"index.html")
    expected_contents = "-".join([obj["name"] for obj in model["values"]]) + "-"
    with open(test_page_path,'r') as page_reader:
        assert page_reader.read() == expected_contents

def test_build_page_lists_and_targets(tmpdir):
    build_path =  create_path(tmpdir,"build")
    input_path =  create_path(tmpdir,"input")

    item_template = """{{ target["name"] }}"""
    item_details = { "items.html": item_template }

    test_website = get_basic_website(get_valid_pages_with_lists())
    test_website["template"] = input_path
    models = [
        {"id":1, "name":"foo"},
        {"id":2, "name":"bar"},
        {"id":3, "name":"barfoo"}
    ]
    test_website["model"] = { "items": models }
    build_dummy_website(tmpdir, test_website, item_details)
    weberator = Webstaterator()
    weberator.build(test_website, build_path)

    expected_files = [
        'index.html',
        'items.html',
        'item-1.html',
        'item-2.html',
        'item-3.html'
    ]
    assert_expected_files(build_path,expected_files)

    for model in models:
        page_path = os.path.join(build_path,"item-{}.html".format(model['id']))
        with open(page_path,'r') as page_reader:
            assert page_reader.read() == model['name']

def test_build_links(tmpdir):
    build_path =  create_path(tmpdir,"build")
    input_path =  create_path(tmpdir,"input")
    item_template = """{% for name,urls in links.items() %}{{ name }}-{% endfor %}"""
    item_details = { "links.html": item_template }

    test_website = get_basic_website(get_valid_pages())
    test_website["template"] = input_path
    build_dummy_website(tmpdir, test_website, item_details)
    weberator = Webstaterator()
    weberator.build(test_website, build_path)

    expected_files = [
        'index.html',
        'items.html',
    ]

    assert_expected_files(build_path,expected_files)

    test_page_path = os.path.join(build_path,"items.html")
    expected_contents = "-".join([page["name"] for page in get_valid_pages()]) + "-"
    with open(test_page_path,'r') as page_reader:
        assert page_reader.read() == expected_contents
