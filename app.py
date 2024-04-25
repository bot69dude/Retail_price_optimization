from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from src.mlProject.pipeline.prediction import PredictionPipeline
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

app = Flask(__name__)

@app.route('/', methods=['GET'])  
def homePage():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET']) 
def index():
    if request.method == 'POST':
        try:
            # Define the feature names
            feature_names = [
                'product_category_name', 'qty', 'freight_price', 'unit_price', 'product_score', 
                'customers', 'weekend', 'holiday', 'month', 'volume', 'comp_1', 'ps1', 'fp1', 
                'comp_2', 'ps2', 'fp2', 'comp_3', 'ps3', 'fp3'
            ]
            
            input_data = []
            for feature in feature_names:
                input_data.append(request.form[feature])
                
            input_data_df = pd.DataFrame([input_data], columns=feature_names)

            # Initialize an instance of the PredictionPipeline class
            obj = PredictionPipeline('artifacts/model_trainer/model.joblib')

            # Use the predict method to make predictions
            predict = obj.predict(input_data_df)

            return render_template('results.html', prediction=predict)
        
        except Exception as e:
            print('The Exception message is: ', e)
            return 'Something went wrong'

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
