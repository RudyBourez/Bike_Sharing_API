from flask_restful import Resource
import pandas as pd
import pickle

class Hello(Resource):
    def get(self, json):
        df = pd.read_json(json, orient="records")
        model = pickle.load(open("model.sav", "rb"))
        y_pred = model.predict(df)
        df["count"] = y_pred
        return df.to_json()