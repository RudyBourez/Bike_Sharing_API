import pandas as pd
import requests
from meteofrance_api import MeteoFranceClient
from datetime import datetime

def create_df():
    client = MeteoFranceClient()
    weather_forecast = client.get_forecast(latitude=50.62925, longitude=3.057256)
    forecast = weather_forecast.forecast
    df = pd.DataFrame()
    df["temp"] = [d["T"]["value"] for d in forecast]
    df["humidity"] = [d["humidity"] for d in forecast]
    df["windspeed"] = [d["wind"]["speed"] for d in forecast]
    df["hour"] = [datetime.fromtimestamp(d["dt"]).hour for d in forecast]
    df["year"] = [datetime.fromtimestamp(d["dt"]).year for d in forecast]
    df["month"] = [datetime.fromtimestamp(d["dt"]).month for d in forecast]
    df["day_number"] = [datetime.fromtimestamp(d["dt"]).day for d in forecast]
    df["day"] = [datetime.fromtimestamp(d["dt"]) for d in forecast]
    df["day"] = df["day"].dt.strftime("%A %d. %B %Y").str.extract(r'(\w+)\s')
    df["workingday"] = [int(d=="Saturday") or int(d=="Sunday") for d in df["day"]]
    #liste des jours de vacances : (month,day)
    liste_holiday = [(7, 4),(4, 16),(1, 2),(9, 3),(10, 8),(1, 17),(4, 15),(9, 5),(10, 10),(11, 12),(1, 16),(11, 11)]
    season = []
    holiday = []
    for i in range(0,len(forecast)):
        month = df.loc[i]["month"]
        day = df.loc[i]["day_number"]

        # vacances ?
        if (month,day) in liste_holiday:
            holiday.append(1)
        else:
            holiday.append(0)

        # saison :
        if (month>9) & (month<12):
            season.append(3) 
        if month == 12:
            if day < 21:
                season.append(3)
            else:
                season.append(4)
        if (month>=1) & (month<3):
            season.append(4)
        if month == 3:
            if day<21:
                season.append(4)
            else:
                season.append(1)
        if (month>3) & (month<6):
            season.append(1)
        if month == 6:
            if day < 21:
                season.append(1)
            else:
                season.append(2)
        if (month>6) & (month<9):
            season.append(2)
        if month == 9:
            if day<21:
                season.append(2)
            else:
                season.append(3)
    df["season"] = season
    df["holiday"] = holiday
    return df

df = create_df()
# print(df.columns)
# response = requests.get(f"http://127.0.0.1:5000/{df.iloc[[0]].to_json(orient='columns')}")
# rep = eval(response.json())["count"].get(f'{0}')

liste_count = []
liste_weather = []
for i in range(len(df)):
    response = requests.get(f"http://127.0.0.1:5000/{df.iloc[[i]].to_json(orient='columns')}")
    liste_count.append(eval(response.json())["count"].get(f'{i}'))
    liste_weather.append(eval(response.json())["weather"].get(f'{i}'))

print("weather : ",liste_weather)