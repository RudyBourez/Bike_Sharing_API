from flask_restful import Resource
import pandas as pd
import numpy as np
import pickle

class Hello(Resource):
    def get(self, json):
        df = pd.DataFrame(eval(json))
        print(df)
<<<<<<< HEAD
        model = pickle.load(open("model_lgbm_no_weather.sav", "rb"))
=======
        model = pickle.load(open("modele.sav", "rb"))
>>>>>>> 957efffe69112329dfd3e66aa1673b54ed1eca6a
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