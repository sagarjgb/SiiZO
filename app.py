from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import math

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def hello_world():
    return render_template("index.html")

@app.route('/result', methods = ['POST', 'GET'])
def result():
    # output = request.form.to_dict()
    if request.method == 'GET':
        output = float(request.args.get('height'))
        print(output)
        heightFeet = output
        df = pd.read_csv('hw.csv')
        x = df['Height(Inches)']
        y = df['Weight(Pounds)']
        model = LinearRegression().fit(np.array(df['Height(Inches)']).reshape(-1,1),df['Weight(Pounds)'])
        heightInch = heightFeet * 12
        weightPound = model.predict(np.array(heightInch).reshape(-1,1))
        weightKg = weightPound * 0.453592
    print('==========================================================================================')
    print('Your weight :', weightKg, 'kg')
    print('==========================================================================================')
    wk = math.ceil(weightKg)
    return render_template('index.html',wt=wk, ht=heightFeet)

if __name__ == '__main__':
    app.run(debug=True)