from src.mlProject.constants import *
from src.mlProject.utils.common import read_yaml, create_directories
from src.mlProject.entity.config_entity import (DataIngestionConfig,
                                            DataValidationConfig,
                                            DataPreprocessConfig,
                                            DataTransformationConfig,
                                            ModelTrainerConfig)
from pathlib import Path

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE,
        params_filepath = PARAMS_FILE,
        schema_filepath = SCHEMA_FILE):

        # Convert the string to a pathlib.Path object
        config_filepath = Path(config_filepath)
        params_filepath = Path(params_filepath)
        schema_filepath = Path(schema_filepath)

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config
    
    def get_data_preprocessing_config(self) -> DataPreprocessConfig:
        config = self.config.data_preprocessing
        drop_columns = self.params['DROP_COLUMNS']
        cat_columns = self.params['CAT_COLUMNS']
        
        create_directories([config.root_dir])
        data_preprocessing_config = DataPreprocessConfig(
            root_dir = config.root_dir,
            data_path = config.data_dir,
            cat_params = cat_columns,
            drop_params = drop_columns  
        )
        
        return data_preprocessing_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.XGBRegressor
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            objective = params.objective,
            colsample_bytree = params.colsample_bytree,
            learning_rate = params.learning_rate,
            max_depth = params.max_depth,
            alpha = params.alpha,
            n_estimators = params.n_estimators,
            target_column = schema.name
            
        )

        return model_trainer_config