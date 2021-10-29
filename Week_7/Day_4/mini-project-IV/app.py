#import the required plugins

from flask import Flask, request, jsonify, render_template, make_response
from flask_restful import Api, Resource
import pickle
import pandas as pd

#Step 1: Wrapping our app
app = Flask(__name__)
api = Api(app)

#Step 1.5: load the model
model = pickle.load(open('pipeline.pickle', 'rb'))

#Step 2: define our API resources



class Predict(Resource):

    def get(self):
        #return "hello world"
        headers = {'Content-Type': 'text/html'}

        return make_response(render_template('my-form.html'),200,headers)

    def post(self):
        json_data = request.get_json()
        if json_data is None:
            json_data = request.form.to_dict(flat=True)
            apiMode = False
        else:
            apiMode = True
        #df = pd.DataFrame(json_data.values(), index = json_data.keys()).transpose()
        df = pd.json_normalize(json_data)
        df['ApplicantIncome'] = df['ApplicantIncome'].astype(int)
        df['CoapplicantIncome'] = df['CoapplicantIncome'].astype(float)
        df['LoanAmount'] = df['LoanAmount'].astype(float)
        df['Loan_Amount_Term'] = df['Loan_Amount_Term'].astype(float)
        df['Credit_History'] = df['Credit_History'].astype(float)
        result =model.predict(df)

        if not apiMode:
            headers = {'Content-Type': 'text/html'}
            if result.tolist()[0] == 1:
                return make_response(render_template('loan-approved.html', probablities=result),200,headers)
            else:
                return make_response(render_template('loan-declined.html', probablities=result),200,headers)
        else:
            return result.tolist()

#Step 3: assign our endpoints
api.add_resource(Predict, '/predict')

#step 4: running our API app
if __name__ == '__main__':
    app.run(debug=True)