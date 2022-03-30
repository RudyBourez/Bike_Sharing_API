from flask_restful import Resource
import pandas as pd
import pickle

class Hello(Resource):
    def get(self, json):
        # Git LFS
        df = pd.DataFrame(eval(json))
        model = pickle.load(open("modele.sav", "rb"))
        y_pred = model.predict(df)
        df["count"] = y_pred
        return df.to_json(orient="columns")