from flask import Flask, request

import pandas as pd

df = pd.read_csv('./data/rxsummary2018.csv')

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return 'this is an API service from MN RX summary details'

@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(10)
    result = top10rows.to_json(orient="records")
    return result

@app.route('/drug/<value>', methods=["GET"])
def drug_name(value):
    # ACETAMINOPHEN
    print('value: ',value)
    filtered = df[df['NPROPNAME'] == value]
    if len(filtered) <=0:
        return 'There is nothing here'
    else:
        return filtered.to_json(orient="records")

@app.route('/drug/<value>/class/<value2>')
def drug_name2(value,value2):
    # Analgesics and Anesthetics
    filtered = df[df['NPROPNAME'] == value]
    filtered2 = filtered[filtered['THER_CLASS'] == value2]
    if len(filtered2) <=0:
        return 'There is nothing here'
    else:
        return filtered2.to_json(orient="records")

if __name__== '__main__':
    app.run(debug=True)

