from flask_restful import Resource
import pandas as pd
import numpy as np
import pickle

class Hello(Resource):
    def get(self, json):
        df = pd.DataFrame(eval(json))
        print(df)
        model = pickle.load(open("model_lgbm_no_weather.sav", "rb"))
        y_pred = model.predict(df)
        df["count"] = np.exp(y_pred) - 1

        # prediction weather
        model_weather = pickle.load(open("model_cluster_weather.sav","rb"))
        print("test")
        weather = model_weather.predict(df[["temp","humidity","windspeed"]])
        #weather = 0
        print("prédiction du weather : ",weather)
        df["weather"] = weather
        return df.to_json(orient="columns")