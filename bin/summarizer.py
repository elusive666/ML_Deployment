# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 13:12:00 2020

@author: Savio Coelho
"""
import yaml
import numpy as np

class SummarizeDoc:
    
    def __init__(self):
        with open('./config/config.yml', 'r') as fl:
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
    
    def findSentLength(self, text):
        return text.split()
    
    def findSentLengthArray(self, sentences):
        return [self.findSentLength(sent) for sent in sentences]
    
    def findTopSentence(self, sentLengths, sentences, n):
        sortIdx = np.argsort(sentLengths)
        topIdx = sortIdx[-n:]
        topSentences = [sentences[i] for i in topIdx]
        return topSentences
    
    def findSummary(self):
        filePath =  self.config['data_path']['train_data']
        text = self.loadDocs(filePath)
        sentences = self.splitSentences(text)
        firstSent, restOfSent = self.groupSentences(sentences)
        sentLengths = self.findSentLengthArray(restOfSent)
        topSentences = self.findTopSentence(sentLengths, restOfSent, self.config['sentence_num'])
        allSentences = [firstSent] + topSentences
        summary = ' '.join(allSentences)
        return summary
    
summarizeDocObj = SummarizeDoc()


#Tortoise GIT or GIT Hub dektop can also be used; in case ur having issues; it has a self explanatory GUI; but knowing the commands are always useful while working on Linux boxes where no UI is available
