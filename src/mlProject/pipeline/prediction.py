import joblib 
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import LabelEncoder

class PredictionPipeline:
    def __init__(self, model_path):
        self.model = joblib.load(Path(model_path))
        self.label_encoders = {}  # Store label encoders for categorical variables

    def preprocess_data(self, data):
        # Convert data to DataFrame
        df = pd.DataFrame(data)

        # Preprocess categorical variables
        for col_index, col_name in enumerate(df.columns):
            if df.dtypes[col_index] == 'object':
                # If the column is categorical, encode it using LabelEncoder
                if col_name not in self.label_encoders:
                    self.label_encoders[col_name] = LabelEncoder()
                df[col_name] = self.label_encoders[col_name].fit_transform(df[col_name])

        return df

    def predict(self, data):
        preprocessed_data = self.preprocess_data(data)
        prediction = self.model.predict(preprocessed_data)

        return prediction