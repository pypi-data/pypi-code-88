"""
sphincontrib-playground

Embed Interactive playground demo in sphinx documentation.

Usage:

.. playground:: link/to/the/python/file.py
  :title: Mandatory title (helpful for screen readers)
  :height: Optional height (default: 500)
    forward to height attribute of <iframe> HTML tag
  :width: Optional width (default: 100%)
    forward to width attribute of <iframe> HTML tag
"""

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.errors import ExtensionError
from sphinx.util.docutils import SphinxDirective


class PlaygroundNode(nodes.General, nodes.Element):
  """Playground Node to attach to Sphinx."""


class Playground(SphinxDirective):
  """Playground directive for Sphionx."""

  has_content = False
  required_arguments = 1
  optional_arguments = 0
  final_argument_whitespace = False

  option_spec = {
    'title': directives.unchanged,
    'height': directives.unchanged,
    'width': directives.unchanged,
  }

  def run(self):
    return [
      PlaygroundNode(
        embed_link=self.arguments[0],
        title=self.options.get('title'),
        height=self.options.get('height'),
        width=self.options.get('width'),
      )
    ]


def embed_playground(self, node):
  """Sphinx html function to embed Playground."""

  title = node['title']
  height = node['height'] or 500
  width = node['width'] or '100%'
  id_ = '-'.join(title.split(' ')).lower()

  url = '/'.join(
    [
      self.config['playground_options']['url'],
      '?github.com',
      self.config['playground_options']['github_repo'],
      'blob',
      self.config['playground_options']['commit_sha'],
      node['embed_link'],
    ]
  )

  embed_code = f"""
<iframe
  src='{url}'
  loading='lazy'
  allow='fullscreen'
  id='p-embed-{id_}'
  class='p-embed-iframe'
  name='p-embed-{id_}'
  width='{width}'
  height='{height}'
  style='border: 1px solid #ddd;'
  title='{title}'
></iframe>"""

  self.body.append(embed_code)

  raise nodes.SkipNode


def setup(app: Sphinx):
  """Sphinx setup function."""

  app.add_node(PlaygroundNode, html=(embed_playground, None))

  # pylint: disable=protected-access
  if not app.config._raw_config['playground_options']['commit_sha']:
    raise ExtensionError('Commit SHA is needed.')

  app.add_config_value(
    'playground_options',
    {'commit_sha': None, 'github_repo': None, 'url': None},
    'html',
  )
  app.add_directive('playground', Playground)

  return {
    'version': '0.1.3',
    'parallel_read_safe': True,
    'parallel_write_safe': True,
  }
