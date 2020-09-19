# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 16:52:13 2020

@author: Savio Coelho
"""

import flask
from flask import Flask, request
from summarizer import SummarizeDoc

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def checkStatus():
    return "YAY!!! it's working"

@app.route('/add', methods=['GET'])
def addNum():
    a = 3
    b = 45
    return "The sum of {} & {} is {}".format(a, b, a+b)

@app.route('/get_summary', methods=['GET'])
def findSummary():
    summarizeObj = SummarizeDoc()
    summary = summarizeObj.findSummary()
    return summary

app.run(host='localhost', port=8023)