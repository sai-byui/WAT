'''
This package contains most of the logic of turning a sentence string into
a performable action. It spans the parsing and evaluation layers.
'''

__author__ = 'SAI'

from action import Action
from word import ADVERB, ADJECTIVE, VERB, NOUN, CDATA, CDWORD, UNDEFINED, WordType, Word, CData, CDWord
from sentence import Sentence
