import pandas as pd 
import numpy as np 
from sklearn.preprocessing import MinMaxScaler
class Preprocessing:
    def pre_processing(self , df):
        df_processed = df.copy()
        df_processed = self.missing_valuess(df_processed)
        return df_processed 
    def missing_valuess(self , df):
       df = df.replace([np.inf, -np.inf], np.nan)
    #    df = df.replace([np.inf, -np.inf], [1e10, -1e10])
       df = df.dropna().reset_index(drop=True)
       df = df.round(7)
       return df

    @staticmethod
    def scaling_data(df):
        columns_to_scale = df.columns[3:-1]
        scaler = MinMaxScaler()
        df_scaled = df.copy()
        df_scaled[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])
        df_scaled[columns_to_scale] = df_scaled[columns_to_scale].round(7)
        return df_scaled , scaler
    


    @staticmethod
    def features_labels_split( df):
       features = df.iloc[:, 3:-1]
       lables = df.iloc[:, -1]
       return features,lables
       
        
