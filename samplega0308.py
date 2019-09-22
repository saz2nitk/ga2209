# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 10:09:42 2019

@author: Winchester
"""
import numpy as np
import flask
import json
from flask import Flask, request

app = Flask(__name__)

class SampleGa:
    
    def __init__(self):
        self.student_age = 32
       
    def calculateAvg(self,marks_list):
        
        mean_marks = np.mean(marks_list)
        marks_per_age = mean_marks/self.student_age
        return marks_per_age
    
    def setAge(self,age):
        
        self.student_age = age

@app.route('/avg',methods=['GET','POST'])
def calculateAvgReq():
    if request.method=='POST':
        data = request.data.decode()
        data = json.loads(data)
        marks_list = data['marks']
        sample_ga_obj = SampleGa()
        #sample_ga_obj.setAge(22)
        avg_marks_per_age = sample_ga_obj.calculateAvg(marks_list)
        print('Avge marks per age is {}'.format(avg_marks_per_age))
        return str(avg_marks_per_age)


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)
        
        
        
    