import streamlit as st
import pandas as pd 
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit_keplergl import keplergl_static 
from keplergl import KeplerGl
from datetime import datetime as dt 

# Page setting
st.set_page_config(page_title = 'CitiBike Strategy Dashboard', layout='wide')

# Add title
st.title("CitiBike Strategy Dashboard")

# Add markdown text
st.markdown("The dashboard will help with the expansion problems CitiBike currently faces")

####################### Import data #########################################

df = pd.read_csv('df_daily_dualaxis.csv', index_col = 0)
top20 = pd.read_csv('top20.csv', index_col = 0)

############################ DEFINE THE CHARTS ############################

# Bar chart 

fig = go.Figure(go.Bar(x = top20['start_station_name'], y = top20['value'], marker = {'color' : top20['value'], 'colorscale' : 'Blues'}))
fig.update_layout(
    title = 'Top 20 Most Popular Bike Stations in New York',
    xaxis_title = 'Start Stations', 
    yaxis_title = 'Sum of Trips', 
    width = 900, height = 600
)
st.plotly_chart(fig, use_container_width = True)

## Line chart 

fig_2 = make_subplots(specs = [[{"secondary_y": True}]])

fig_2.add_trace(
go.Scatter(x = df['date'], y = df['bike_rides_daily'], name = 'Daily bike rides', marker={'color': df['bike_rides_daily'], 'color': 'darkblue'}), secondary_y = False
)

fig_2.add_trace(
go.Scatter(x = df['date'], y = df['avgTemp'], name = 'Daily temperature', marker={'color': df['avgTemp'], 'color': 'firebrick'}), secondary_y = True
)

fig_2.update_layout(
    title = 'Top 20 most popular bike stations in New York', 
    xaxis_title = 'Start stations',
    yaxis_title = 'Sum of trips',
    height = 800
)
st.plotly_chart(fig_2, use_container_width=True)

### Add the map  ###

path_to_html = "CitiBike Trips Aggregated.html"

# Read file and keep in variable 
with open(path_to_html, 'r') as f:
    html_data = f.read()

## Show in web page 
st.header("Aggregated Bike Trips in New York")
st.components.v1.html(html_data,height = 1000)