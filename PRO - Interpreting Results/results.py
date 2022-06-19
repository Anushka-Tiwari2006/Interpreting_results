from tkinter import HORIZONTAL
from turtle import distance
from matplotlib.pyplot import xlabel, xticks
import pandas as pd
import matplotlib as plt
import csv
import plotly.express as px

df = pd.read_csv("archive_dataset_new.csv")
star_name  = df["Star_name"]
star_mass= df["Mass"]
star_distance = df["Distance"]
star_radius = df["Radius"]


fig = px.bar(x = star_name, y = star_mass,color = star_mass,title="Star name Vs Star mass",labels={'y':'Mass','x':'Name'})
fig.show()
fig2 = px.bar(x = star_name, y = star_distance,color = star_distance,title="Star name Vs Star distance",labels={'y':'Distance','x':'Name'})
fig2.show()
fig3 = px.bar(x = star_name, y = star_radius,color = star_radius,title="Star name Vs Star radius",labels={'y':'Radius','x':'Name'})
fig3.show()

