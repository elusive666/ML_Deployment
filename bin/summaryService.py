# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 11:01:07 2020

@author: Savio Coelho
"""

import flask
from flask import Flask, request
from summarizer import SummarizeDoc

app = Flask(__name__)

@app.route('/get_summary',methods=['GET'])
def findSummary():
    summarizeObj = SummarizeDoc()
    summary = summarizeObj.findSummary()
    return summary

app.run('localhost',5000)