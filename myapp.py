import pandas as pd

from os.path import dirname, join
from script.covid import *
from bokeh.io import curdoc


df = pd.read_csv(join(dirname(__file__), "data", "covid.csv"))
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
layout = covid(df)


curdoc().add_root(layout)
curdoc().title = "Kasus Covid-19 Dunia"
