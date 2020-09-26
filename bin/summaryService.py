# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 11:01:07 2020

@author: Savio Coelho
"""

import flask
from flask import Flask, request
from summarizer import SummarizeDoc

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def check_Status():
    return "YAY!!! it's working"

@app.route('/add', methods=['GET'])
def add_Num():
    a = 3
    b = 45
    return "The sum of {} & {} is {}".format(a, b, a+b)

@app.route('/get_summary', methods=['GET'])
def find_Summary():
    summarizeObj = SummarizeDoc()
    summary = summarizeObj.findSummary()
    return summary

app.run(host='localhost', port=8023)