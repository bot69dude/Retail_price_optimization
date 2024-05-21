from flask import Flask, render_template, request
from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from src.mlProject.pipeline.prediction import PredictionPipeline
import warnings
import joblib
from pathlib import Path

warnings.simplefilter(action='ignore', category=FutureWarning)

app = Flask(__name__)

model = joblib.load(Path("artifacts/model_trainer/model.joblib"))

@app.route('/', methods=['GET'])  
def homePage():
    return render_template("index.html")

@app.route('/predict', methods=['POST', 'GET']) 
def web_predict():
    if request.method == 'POST':
        try:
            feature_names = list(model.feature_names_in_)
            
            input_data = []
            for feature in feature_names:
                input_data.append(request.form.get(feature))

            # Ensure proper data types for the model
            input_data = [
                str(input_data[0]),  # Assuming this is the product category (string)
                int(input_data[1]),  # qty
                float(input_data[2]),  # freight_price
                float(input_data[3]),  # unit_price
                float(input_data[4]),  # product_score
                int(input_data[5]),  # customers
                int(input_data[6]),  # weekend
                int(input_data[7]),  # holiday
                int(input_data[8]),  # month
                int(input_data[9]),  # volume
                float(input_data[10]),  # comp_1
                float(input_data[11]),  # comp_2
                float(input_data[12]),  # comp_3
                float(input_data[13]),  # ps1
                float(input_data[14]),  # ps2
                float(input_data[15]),  # ps3
                float(input_data[16]),  # fp1
                float(input_data[17]),  # fp2
                float(input_data[18])   # fp3
            ]

            # Initialize an instance of the PredictionPipeline class
            obj = PredictionPipeline()

            # Use the predict method to make predictions
            predict = obj.predict(input_data)

            return render_template('results.html', prediction=predict)

        
        except Exception as e:
            print('The Exception message is: ', e)
            return 'Something went wrong'

    else:
        return render_template('index.html')


@app.route('/api/predict', methods=['POST']) 
def api_predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Debugging: print raw input data
        print("Raw input data received:", data)

        # Ensure proper data types for the model
        input_data = [
            str(data['product_category_name']),
            int(data['qty']),
            float(data['freight_price']),
            float(data['unit_price']),
            float(data['product_score']),
            int(data['customers']),
            int(data['weekend']),
            int(data['holiday']),
            int(data['month']),
            int(data['volume']),
            float(data['comp_1']),
            float(data['comp_2']),
            float(data['comp_3']),
            float(data['ps1']),
            float(data['ps2']),
            float(data['ps3']),
            float(data['fp1']),
            float(data['fp2']),
            float(data['fp3'])
        ]

        # Debugging: print parsed input data
        print("Parsed input data:", input_data)

        # Initialize an instance of the PredictionPipeline class
        obj = PredictionPipeline()

        # Use the predict method to make predictions
        predict = obj.predict(input_data)

        # Convert prediction to standard Python data type for JSON serialization
        prediction_result = predict.item() if hasattr(predict, 'item') else predict

        return jsonify({'prediction': prediction_result})
    
    except Exception as e:
        print('The Exception message is:', e)
        return 'Something went wrong', 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
