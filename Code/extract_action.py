"""
    Algorithm that generates data on Docs/output.html with action sentences
"""

# -*- coding: utf-8 -*-
import nltk         
import os          
import re         
   
gameDir = open('../Datasets/Taz.txt')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')    
output = open('../Docs/output.html','w')  

def extract_action():
	first_line =  gameDir.readline()
	txt = gameDir.read()
	#sentence='<>'.join(tokenizer.tokenize(sentences))
	sentences = txt.split('.')	
	title = "<title>"+first_line+"</title>\n"
	output.write(title)
	for sentence in sentences:
		words = nltk.word_tokenize(sentence)
		sentence_postag = nltk.pos_tag(words)
		write_html_action(sentence, sentence_postag)


def write_html_action(sent, sent_postag):
	if check_verbs(sent_postag):
		string = "<action>"+sent+"</action>\n"
		output.write(string)

def check_verbs(sentence):
	for pos_tag in sentence:
		if pos_tag[1] == 'VB':
			return True


extract_action()

