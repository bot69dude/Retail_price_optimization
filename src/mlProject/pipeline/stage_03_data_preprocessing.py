from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_preprocessing import DataPreprocessing
from src.mlProject import logger

STAGE_NAME = "Data Preprocessing stage"

class DataPreprocessingTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_preprocess_config = config.get_data_preprocessing_config()
        data_preprocess = DataPreprocessing(config=data_preprocess_config)
        data_preprocess.preprocess_data()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataPreprocessingTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e