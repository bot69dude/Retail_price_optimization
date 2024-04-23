import os
from src.mlProject import logger
from src.mlProject.entity.config_entity import DataPreprocessConfig
from sklearn.preprocessing import LabelEncoder
import pandas as pd

class DataPreprocessing:
    def __init__(self, config: DataPreprocessConfig):
        self.config = config
        
    def preprocess_data(self):
        try:
            # Read data from CSV
            df = pd.read_csv(self.config.data_path)
            
            # Drop columns specified in the config
            df = df.drop(columns=self.config.drop_params)
            
            # Apply LabelEncoder to categorical columns specified in the config
            label_encoder = LabelEncoder()
            for col in self.config.cat_params:
                df[col] = label_encoder.fit_transform(df[col])
            
            # Save preprocessed data to CSV
            output_file_path = os.path.join(self.config.root_dir, "preprocessed_data.csv")
            df.to_csv(output_file_path, index=False)
            
            logger.info(f"Preprocessed data saved to: {output_file_path}")  
            
        except Exception as e:
            logger.error(f"Error occurred during data preprocessing: {str(e)}")
            raise e
