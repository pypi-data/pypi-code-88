# Copyright (C) 2021
# Author: Kacper Sokol <k.sokol@bristol.ac.uk>
# License: new BSD
"""
Implements the `problog` directive for Jupyter Book and Sphinx.
"""

import os
import sys

from docutils import nodes
from docutils.parsers.rst import Directive

import sphinx_problog

DEPENDENCIES = [  # See sphinx_problog/_static/README.md for more info
    # jQuery (MIT): https://github.com/jquery/jquery
    'https://code.jquery.com/jquery-2.1.0.min.js',
    # jQuery UI (MIT): https://github.com/jquery/jquery-ui
    'https://code.jquery.com/ui/1.11.1/jquery-ui.min.js',
    # CryptoJS (MIT): https://github.com/brix/crypto-js
    # 'https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/components/md5.js'
]

STATIC_CSS_FILES = ['sphinx-problog.css']
STATIC_JS_FILES = [
    'ace.js', 'mode-problog.js', 'problog_editor_advanced.js', 'jquery-fix.js']
STATIC_FILES = STATIC_CSS_FILES + STATIC_JS_FILES

if sys.version_info >= (3, 0):
    unicode = str


#### ProbLog directive ########################################################


class problog_box(nodes.General, nodes.Element):
    """A `docutils` node holding ProbLog boxes."""


def visit_problog_box_node(self, node):
    """Builds an opening HTML tag for ProbLog boxes."""
    self.body.append(self.starttag(node, 'div', CLASS='container-fluid'))


def depart_problog_box_node(self, node):
    """Builds a closing HTML tag for ProbLog boxes."""
    self.body.append('</div>\n')


def visit_problog_box_node_(self, node):
    """Builds a prefix for embedding ProbLog boxes in LaTeX and raw text."""
    raise NotImplemented


def depart_problog_box_node_(self, node):
    """Builds a postfix for embedding ProbLog boxes in LaTeX and raw text. """
    raise NotImplemented


class problog_code(nodes.literal_block, nodes.Element):
    """
    A `docutils` node holding the **code** embedded in the ProbLog boxes.
    """


def visit_problog_code_node(self, node):
    """Builds an opening HTML tag for ProbLog **code** boxes."""
    classes = ['problog-editor']
    attributes = {
        'data-width': '100%',
        'data-task': 'prob',
        'data-advanced': 'false',
        'data-trackurl': 'false',
        'data-autosize': 'true'
    }

    self.body.append(self.starttag(
        node, 'div', CLASS=' '.join(classes), **attributes).strip('\n'))


def depart_problog_code_node(self, node):
    """Builds a closing HTML tag for ProbLog **code** boxes."""
    self.body.append('</div>\n')


def visit_problog_code_node_(self, node):
    """
    Builds a prefix for embedding ProbLog **code** boxes in LaTeX and raw text.
    """
    raise NotImplemented


def depart_problog_code_node_(self, node):
    """
    Builds a postfix for embedding ProbLog **code** boxes in LaTeX and
    raw text.
    """
    raise NotImplemented


class ProbLog(Directive):
    """
    Defines the `problog` directive that builds interactive ProbLog code boxes.

    The `problog` directive is of the form::
       .. problog:: problog:1.2.3 (required)

    All of the ids need to be ProbLog code files **with** the `problog:` prefix
    and **without** the `.pl` extension, located in a single directory.
    The directory is provided to Sphinx via the `sphinx_problog_code_directory`
    config setting.
    If this parameter is not set, code box content must be provided explicitly.

    Optionally, the `sphinx_problog_execution_server_url` config setting can be
    provided, which specifies the URL of the ProbLog execution server.
    If one is not given, the default URL hardcoded in the ProbLog JavaScript
    library will be used (i.e., `https://verne.cs.kuleuven.be/problog/api/`).

    This directive operates on one variable:

    sphinx_problog_has_problog
      A set of names of documents that include ProbLog boxes.
      This is used to inject the necessary JavaScript call to the footer of
      each page with an embedded ProbLog code box.

    This Sphinx extension monitors the code files for changes and
    regenerates the content pages that use them if a change is detected.
    """
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = True
    option_spec = {}

    def run(self):
        """Builds a ProbLog box."""
        env = self.state.document.settings.env

        # memorise that this document (a content source file) uses at least
        # one ProbLog box
        if not hasattr(env, 'sphinx_problog_has_problog'):
            env.sphinx_problog_has_problog = set()
        if env.docname not in env.sphinx_problog_has_problog:
            env.sphinx_problog_has_problog.add(env.docname)

        # retrieve the path to the directory holding the code files
        sp_code_directory = env.config.sphinx_problog_code_directory
        assert isinstance(sp_code_directory, str) or sp_code_directory is None

        # get the code file name for this particular ProbLog box
        assert len(self.arguments) == 1, (
            'Just one argument -- code block id (possibly encoding the code '
            'file name -- expected')
        code_filename_id = self.arguments[0]
        assert code_filename_id.startswith('problog:'), (
            'The code box label ({}) must start with the "problog:" '
            'prefix.'.format(code_filename_id))
        assert not code_filename_id.endswith('.pl'), (
            'The code box label ({}) must not end with the ".pl" '
            'extension prefix.'.format(code_filename_id))
        # add the .pl extension as it is missing
        code_filename = '{}.pl'.format(code_filename_id[8:])

        # if the content is given explicitly, use it instead of loading a file
        if self.content:
            contents = '\n'.join(self.content)
        else:
            localised_directory = localise_code_directory(
                sp_code_directory, 'ProbLog box content')
            # compose the full path to the code file and ensure it exists
            path_localised = os.path.join(localised_directory, code_filename)
            # path_original = os.path.join(sp_code_directory, code_filename)
            sphinx_problog.file_exists(path_localised)

            # memorise the association between the document (a content source
            # file) and the code box -- this is used for watching for code file
            # updates
            env.note_dependency(path_localised)

            # read in the code file and create a ProbLog **code** node
            with open(path_localised, 'r') as f:
                contents = f.read().strip('\n')

        pre = problog_code(contents.strip(), contents,
                           ids=['{}-code'.format(
                               nodes.make_id(code_filename_id))],
                         label=code_filename_id)
        # create the outer ProbLog node
        box = problog_box()
        # assign label and id (`ids=[nodes.make_id(code_filename_id)]`)
        self.options['name'] = code_filename_id
        self.add_name(box)

        # insert the ProbLog code node into the outer node
        box += pre

        return [box]


def localise_code_directory(sp_code_directory, request_type=None):
    """Localise the code directory path."""
    if request_type is None:
        request_type = 'ProbLog box content'
    if sp_code_directory is None:
        raise RuntimeError('The sphinx_problog_code_directory sphinx config '
                           'value must be set when loading {} from a '
                           'file.'.format(request_type))
    # localise the directory if given as an absolute path
    if sp_code_directory.startswith('/'):
        localised_directory = '.' + sp_code_directory
    else:
        localised_directory = sp_code_directory
    # check whether the directory exists
    if not os.path.exists(localised_directory):
        raise RuntimeError('The sphinx_problog_code_directory ({}) does not '
                           'exist.'.format(localised_directory))
    return localised_directory


def purge_problog_detect(app, env, docname):
    """
    Cleans the information stored in the Sphinx environment about documents
    with ProbLog blocks (`sphinx_problog_has_problog`).
    If a document gets regenerated, the information whether this document
    has a ProbLog directive is removed before the document is processed again.

    This function is hooked up to the `env-purge-doc` Sphinx event.
    """
    if hasattr(env, 'sphinx_problog_has_problog'):
        # if the document was recorded to have a ProbLog block and is now being
        # rebuilt, remove it from the store
        if docname in env.sphinx_problog_has_problog:
            env.sphinx_problog_has_problog.remove(docname)


def merge_problog_detect(app, env, docnames, other):
    """
    In case documents are processed in parallel, the data stored in
    the `sphinx_problog_has_problog` Sphinx environment variable from different
    threads need to be merged.

    This function is hooked up to the `env-merge-info` Sphinx event.
    """
    if not hasattr(env, 'sphinx_problog_has_problog'):
        env.sphinx_problog_has_problog = set()
    if hasattr(other, 'sphinx_problog_has_problog'):
        # join two sets by taking their union
        env.sphinx_problog_has_problog |= other.sphinx_problog_has_problog


def inject_problog_detect(app, doctree, docname):
    """
    Injects call to the ProbLog JavaScript library in documents that have
    ProbLog code blocks.

    This function is hooked up to the `doctree-resolved` Sphinx event.
    """
    env = app.builder.env

    # if no ProbLog code blocks were detected, skip this step
    if not hasattr(env, 'sphinx_problog_has_problog'):
        return
    # if this document does not have any ProbLog code blocks, skip this step
    if docname not in env.sphinx_problog_has_problog:
        return

    # check for a user-specified ProbLog server URL in the config
    sp_problog_url = env.config.sphinx_problog_execution_server_url
    if sp_problog_url:
        call = "'{:s}'".format(sp_problog_url)
    else:
        call = ''
    problog_function = ('\n\n'
                        '    <script type="text/javascript">\n'
                        '        $(document).ready(function() {{\n'
                        '            problog.init({:s});\n'
                        '        }});\n'
                        '    </script>\n').format(call)
    # `format='html'` is crucial to avoid escaping html characters
    script_node = nodes.raw(problog_function, problog_function, format='html')
    # add the call node to the document
    doctree.append(script_node)


def assign_reference_title(app, document):
    """
    Update the labels record of the standard environment to allow referencing
    ProbLog boxes.
    """
    # get the standard domain
    domain = app.env.get_domain('std')

    # go through every ProbLog box
    for node in document.traverse(problog_box):
        # every ProbLog box must have exactly one name starting with 'problog:'
        assert node['names']
        assert len(node['names']) == 1
        node_name = node['names'][0]

        assert node_name.startswith('problog:'), (
            'ProbLog box ids must start with problog:')
        refname = 'ProbLog code box'

        # every ProbLog box has a single id
        assert len(node['ids']) == 1
        node_id = node['ids'][0]

        # get the document name
        docname = app.env.docname

        # every ProbLog box should **already** be referenceable without a title
        assert node_name in domain.anonlabels
        assert domain.anonlabels[node_name] == (docname, node_id)

        # allow this ProbLog box to be referenced with the default
        # 'ProbLog code box' stub
        domain.labels[node_name] = (docname, node_id, refname)


#### Extension setup ##########################################################


def include_static_files(app):
    """
    Copies the static files required by this extension.
    (Attached to the `builder-inited` Sphinx event.)
    """
    for file_name in STATIC_FILES:
        file_path = sphinx_problog.get_static_path(file_name)
        if file_path not in app.config.html_static_path:
            app.config.html_static_path.append(file_path)


def setup(app):
    """
    Sets up the Sphinx extension for the `problog` directive.
    """
    # register two Sphinx config values used for the extension
    app.add_config_value('sphinx_problog_code_directory', None, 'env')
    app.add_config_value('sphinx_problog_execution_server_url', '', 'env')

    # register the custom docutils nodes with Sphinx
    app.add_node(
        problog_box,
        html=(visit_problog_box_node, depart_problog_box_node),
        latex=(visit_problog_box_node_, depart_problog_box_node_),
        text=(visit_problog_box_node_, depart_problog_box_node_)
    )
    app.add_node(
        problog_code,
        html=(visit_problog_code_node, depart_problog_code_node),
        latex=(visit_problog_code_node_, depart_problog_code_node_),
        text=(visit_problog_code_node_, depart_problog_code_node_)
    )

    # add external dependencies
    # ...must be available prior to loading custom scripts
    for js_file in DEPENDENCIES:
        if not sphinx_problog.is_js_registered(app, js_file):
            app.add_js_file(js_file)
    # ensure the required auxiliary files are included in the Sphinx build
    app.connect('builder-inited', include_static_files)
    # ..check whether custom files were included
    for css_file in STATIC_CSS_FILES:
        if not sphinx_problog.is_css_registered(app, css_file):
            app.add_css_file(css_file)
    for js_file in STATIC_JS_FILES:
        if not sphinx_problog.is_js_registered(app, js_file):
            app.add_js_file(js_file)

    # register the custom role and directives with Sphinx
    app.add_directive('problog', ProbLog)

    # connect custom hooks to the Sphinx build process
    app.connect('env-purge-doc', purge_problog_detect)
    app.connect('env-merge-info', merge_problog_detect)
    app.connect('doctree-resolved', inject_problog_detect)
    app.connect('doctree-read', assign_reference_title)

    return {'version': sphinx_problog.VERSION}
