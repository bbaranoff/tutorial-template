from __future__ import absolute_import
from docutils import nodes
from docutils.parsers.rst import Directive, directives
# Configuration file for the Sphinx documentation builder.

# -- Project information


project = 'RF-eXploring'
copyright = '2022, Bastien Baranoff'
author = 'Bastien Baranoff'

source_suffix = ['.rst', '.md']

master_doc = 'index'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'


