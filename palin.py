#!/usr/bin/env python

from sentence_generator import *       # https://github.com/patrick-brian-mooney/markov-sentence-generator
import glob

print('Content-Type: text/html; charset=utf-8\n\n')
print('<title>Sarah Palin Gibberish</title>')
print('<h1>Sarah Palin Quote, or Random Gibberish?</h1>')

the_list = []
for which_file in glob.glob('speeches/*txt'):
    the_list = the_list + word_list(which_file)
starts, the_mapping = buildMapping(the_list, markov_length=2)

print('<p>%s</p>' % gen_text(the_mapping, starts, markov_length=2, sentences_desired=5, paragraph_break_probability=0) )
