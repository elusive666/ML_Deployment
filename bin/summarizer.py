# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 13:12:00 2020

@author: Savio Coelho
"""
import yaml

class SummarizeDoc:
    
    def __init__(self):
        with open('../config/config.yml', 'r') as fl:
            self.config = yaml.load(fl)
    
    def loadDocs(self, filePath):
        with open(filePath, 'r') as fl:
            text = fl.read()
        return text
        
    def splitSentences(self, text):
        sentences = text.split('.')
        return sentences
    
    def groupSentences(self, sentences):
        firstSent, restOfSent = sentences[0], sentences[1:]
        return firstSent, restOfSent
    
    def findNumWords(self):
        pass
    
    def findTop3Sent(self):
        pass
    
    def sentenceCombiner(self):
        pass
    
summarizeDocObj = SummarizeDoc()
summarizeDocObj.loadConfig()


