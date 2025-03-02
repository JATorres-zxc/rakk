import os
import re
from calendar import month_abbr
from datetime import datetime
from itertools import zip_longest

import pandas as pd


DATE_FMT = re.compile(r"(\w+) (\d+), (\d+)")
MONTH_DICT = dict(zip(month_abbr, range(len(month_abbr))))
HIGH_LOW = re.compile(r"(high|low)$")


def raw_date_to_datetime(raw):
    match = DATE_FMT.match(raw)
    mm = MONTH_DICT[match.group(1)[:3]]
    dd = int(match.group(2))
    yy = int(match.group(3))

    return datetime(yy, mm, dd)


def chunks(iterable, n):
    iterator = [iter(iterable)] * n

    return zip_longest(*iterator)


def data_dir_to_dataframe(path):
    df = pd.DataFrame(columns=["date", "market", "commodity", "low", "high"])

    for entry in os.scandir(path):
        print("[INFO] processing:", entry.path)
        try:
            raw = pd.read_csv(entry.path)
        except UnicodeDecodeError:
            raw = pd.read_csv(entry.path, encoding="latin-1")
        columns = map(lambda c: c.replace("\n", " ").lower(), raw.columns)
        raw.rename(columns=dict(zip(raw, columns)), inplace=True)
        raw["date"] = list(map(raw_date_to_datetime, raw["date"]))

        for row in raw.index:
            row = raw.iloc[row]
            date = row["date"]
            market = row["market"]
            for (name, low), (_, high) in chunks(row[2:].items(), 2):
                name = name[:-4]
                df.loc[len(df)] = [date, market, name, low, high]

    return df
