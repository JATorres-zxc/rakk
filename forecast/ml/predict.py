import numpy as np
import pandas as pd


DATA = pd.read_csv("forecast/ml/lowhigh_2023_2025.csv")
DATA["date"] = pd.to_datetime(DATA["date"])


def delta_days(start_day):
    delta = (
        start_day.tz_localize(None)
        - pd.to_datetime(DATA.tail(1)["date"].values)
    )

    return delta.days.values[0]


def generate_dates(start_day, delta_days):
    for days in range(delta_days):
        yield start_day + pd.Timedelta(days=days)


def predict_best_day(model, start_day, future_days):
    start_day = pd.to_datetime(start_day)
    rev_data = DATA[::-1]
    predict_days = future_days + delta_days(start_day)

    input_data = []
    day = 0
    for ith in range(0, rev_data.shape[0], 3):
        if day > predict_days:
            break
        day += 1
        input_data.append(rev_data[["low", "high"]][ith:ith + 3].to_numpy())

    input_data = np.array(input_data, dtype="float32")
    predictions = model.predict(input_data, verbose=0).flatten()

    date_to_price = list(zip(
        generate_dates(start_day, delta_days), predictions
    ))
    (best_date, best_price) = date_to_price.pop()
    for date, price in date_to_price:
        if best_price > price:
            best_price = price
            best_date = best_date

    return {"best_date": best_date, "best_price": best_price}
