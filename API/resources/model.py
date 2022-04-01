from flask_restful import Resource
import pandas as pd
import numpy as np
import pickle

class Hello(Resource):
    def get(self, json):
        df = pd.DataFrame(eval(json))
        print(df)
        model = pickle.load(open("model.pkl", "rb"))
        y_pred = model.predict(df)
        df["count"] = np.exp(y_pred) - 1
        return df.to_json(orient="columns")