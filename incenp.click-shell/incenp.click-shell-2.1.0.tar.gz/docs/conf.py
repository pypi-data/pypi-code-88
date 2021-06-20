# -*- coding: utf-8 -*-

# -- General configuration ------------------------------------------------

source_suffix = '.rst'
master_doc = 'index'

copyright = u'2021 Damien Goutte-Gattat'
author = u'Damien Goutte-Gattat <dgouttegattat@incenp.org>'

language = 'en'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'

extensions = ['sphinx.ext.intersphinx']
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Options for LaTeX output ---------------------------------------------

latex_engine = 'lualatex'

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt'
}

latex_documents = [
  (master_doc, 'click-shell.tex', u'click-shell Documentation',
   u'Damien Goutte-Gattat', 'manual'),
]
