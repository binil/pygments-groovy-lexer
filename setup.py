"""
Setup for the Groovy Pygments Lexer
"""
from setuptools import setup

__author__ = 'binil.thomas@gmail.com'

setup(
    name='Groovy Pygments Lexer',
    version='0.1.0',
    description=__doc__,
    author=__author__,
    packages=['groovy_lexer'],
    entry_points='''[pygments.lexers]
groovylexer = groovy_lexer:GroovyLexer
'''
)
