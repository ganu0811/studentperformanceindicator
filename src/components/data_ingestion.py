import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#  This class is created because anything that is required in the data ingestion component will be given through this DataIngestionConfig class

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv") # output of the data_ingestion component will be saved in the artifact folder by the name of train.csv file
    test_data_path:str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")



class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # The moment DataIngestion class is called, those three paths will get saved in the ingestion_config variable
    
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the data set as dataframe")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)
            
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True) # Saved the raw data
            
            logging.info("Train Test Split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True) # Saved the train data
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True) # Saved the test data
            
            logging.info("Ingestion of the data is completed")
            
            return (self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path)
        except Exception as e:
            raise CustomException(e,sys)


if __name__=="__main__":
    data_ingestion_obj = DataIngestion()
    data_ingestion_obj.initiate_data_ingestion()
    
