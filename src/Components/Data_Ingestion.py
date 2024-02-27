import os
import sys
from src.Exception import CustomException


from src.Logger import logging

#import numpy  as np
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass 
            #Why @DataClass ->if you're using dataclass Decorator you don't need to use constructor to initialize the attributes
class DataIngestionConfig:
    train_data_path = os.path.join("Artifacts","Train.csv")
    test_data_path = os.path.join("Artifacts","test.csv")
    Raw_data_path = os.path.join("Artifacts","Raw.csv")


class DataIngestion:
    #Why Constructor right now ? Why not @DataClass -> 
    #Since we have to intialize methods also that's why we're using Constuctor
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() #Stores the paths of the input data
    def Initiate_data_ingestion(self):
        logging.info("Entered the Data Ingestion Method or Components")
        try:
            df = pd.read_csv(r"Notebooks\Data\stud.csv")
            logging.info("Read the Dataset as Dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.Raw_data_path,index=False,header=True)
            logging.info("train Test Split Intitated")
            train_set,test_set = train_test_split(df,test_size=0.3,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index =False,header = True)
            test_set.to_csv(self.ingestion_config.test_data_path,index =False,header = True)
            logging.info("Ingestion of the data is Completed")

            return (self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path)
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.Initiate_data_ingestion()

