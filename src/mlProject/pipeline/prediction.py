import joblib 
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import LabelEncoder

class PredictionPipeline:
<<<<<<< HEAD
    def __init__(self, model_path):
        self.model = joblib.load(Path(model_path))
=======
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))
>>>>>>> dev
        self.label_encoders = {}  # Store label encoders for categorical variables

    def preprocess_data(self, data):
        # Convert data to DataFrame
<<<<<<< HEAD
        df = pd.DataFrame(data)

        # Preprocess categorical variables
        for col_index, col_name in enumerate(df.columns):
            if df.dtypes[col_index] == 'object':
                # If the column is categorical, encode it using LabelEncoder
                if col_name not in self.label_encoders:
                    self.label_encoders[col_name] = LabelEncoder()
                df[col_name] = self.label_encoders[col_name].fit_transform(df[col_name])
=======
        model_features = list(self.model.feature_names_in_)

        df = pd.DataFrame([data], columns=model_features)

        # Preprocess categorical variables
        for col_name in df.columns:
            if col_name == "product_category_name":
                if col_name not in self.label_encoders:
                    self.label_encoders[col_name] = LabelEncoder()
                
                    unique_categories = ['bed_bath_table', 'garden_tools', 'consoles_games','health_beauty', 'cool_stuff', 'perfumery','computers_accessories', 'watches_gifts', 'furniture_decor'] 
                    self.label_encoders[col_name].fit(unique_categories)
                df[col_name] = self.label_encoders[col_name].transform(df[col_name])
>>>>>>> dev

        return df

    def predict(self, data):
        preprocessed_data = self.preprocess_data(data)
        prediction = self.model.predict(preprocessed_data)

<<<<<<< HEAD
        return prediction
=======
        return prediction[0]
>>>>>>> dev
