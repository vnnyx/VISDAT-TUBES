import pandas as pd

from controller.covid import *
from bokeh.io import curdoc
from bokeh.io import show, output_file, save

output_file("covid.html")
df = pd.read_csv("data/covid.csv")
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
layout = covid(df)
save(layout)

curdoc().add_root(layout)
curdoc().title = "Application"


show(curdoc)
