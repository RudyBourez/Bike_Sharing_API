from flask_restful import Resource
import pandas as pd
import numpy as np
import pickle

class Hello(Resource):
    def get(self, json):
        df = pd.DataFrame(eval(json))
        model_count = pickle.load(open("model_stacking_count.sav", "rb"))
        model_registered = pickle.load(open("model_stacking_registered.sav", "rb"))

        y_count = model_count.predict(df)
        y_registered = model_registered.predict(df)

        df["count"] = np.round(np.exp(y_count) - 1)
        df["registered"] = np.round(np.exp(y_registered) - 1)
        for i in range (len(df)):
            if df["registered"].iloc[i] > df["count"].iloc[i]:
                df["registered"].iloc[i] = df["count"].iloc[i]
        df["casual"] = df["count"] - df["registered"]

        # prediction weather
        model_weather = pickle.load(open("model_cluster_weather.sav","rb"))
        print("test")
        weather = model_weather.predict(df[["temp","humidity","windspeed"]])
        #weather = 0
        print("prédiction du weather : ",weather)
        df["weather"] = weather
        return df.to_json(orient="columns")
