# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 13:11:30 2020

@author: Savio Coelho
"""
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class PreprocessDoc:
    
    """
    Module for PreProcessing articles
    """
    
    def specialCharRemoval(self, text):
        return re.sub('[^A-Za-z0-9 ]+', '', text)
    
    def convertToLower(self, text):
        return text.lower()
    
    def stopwordRemoval(self, text):
        stop_words = set(stopwords.words('english'))   
        word_tokens = word_tokenize(text)           
        filtered_sentence = [w for w in word_tokens if not w in stop_words]          
        filtered_sentence = [] 
        for w in word_tokens: 
            if w not in stop_words: 
                filtered_sentence.append(w)           
        print(word_tokens) 
        print(filtered_sentence) 
    
