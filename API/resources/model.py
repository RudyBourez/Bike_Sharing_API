from flask_restful import Resource
import pandas as pd
import pickle, gzip

class Hello(Resource):
    def get(self, json):
        df = pd.DataFrame(eval(json))
        model = pickle.load(gzip.open("model.sav", "rb"))
        y_pred = model.predict(df)
        df["count"] = y_pred
        return df.to_json(orient="columns")