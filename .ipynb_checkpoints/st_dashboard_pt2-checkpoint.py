############################################ CITIBIKES DASHABOARD ###################################################

import streamlit as st
import pandas as pd 
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit_keplergl import keplergl_static 
from keplergl import KeplerGl
from datetime import datetime as dt 
from numerize.numerize import numerize
from PIL import Image

### INITIAL SETTINGS FOR THE DASHBOARD #############################################################################

st.set_page_config(page_title = 'Citi Bikes Strategy Dashboard', layout='wide')
st.title("Citi Bikes Strategy Dashboard")

# Define side bar
st.sidebar.title("Aspect Selector")
page = st.sidebar.selectbox('Select an aspect of the analysis',
  ["Introduction","Weather component and bike usage",
   "Most popular stations",
    "Interactive map with aggregated bike trips", "Classic versus electric bikes", "Recommendations"])

### IMPORT DATA ##################################################################################################

df = pd.read_csv('reduced_data_to_plot_7.csv', index_col = 0)
top20 = pd.read_csv('top20.csv', index_col = 0)
df_hist = pd.read_csv('hist_data_small.csv')

### DEFINE THE PAGES #############################################################################################


### INTRO PAGE

if page == "Introduction":
    st.markdown("#### This dashboard aims at providing helpful insights on the expansion problems Citi Bikes currently faces.")
    st.markdown("Right now, Citi Bikes runs into a situation where customers complain about bikes not being available at certain times. This analysis will look at the potential reasons behind this. The dashboard is separated into 5 sections:")
    st.markdown("- Most popular stations")
    st.markdown("- Weather component and bike usage")
    st.markdown("- Interactive map with aggregated bike trips")
    st.markdown("- Classic versus electric bikes")
    st.markdown("- Recommendations")
    st.markdown("The dropdown menu on the left 'Aspect Selector' will take you to the different aspects of the analysis our team looked at.")

    myImage = Image.open("citi_bike_logo.png") 
    st.image(myImage)

    
### LINE CHART PAGE: WEATHER COMPONENT AND BIKE USAGE
    
elif page == 'Weather component and bike usage':

    fig_2 = make_subplots(specs = [[{"secondary_y": True}]])

    fig_2.add_trace(
    go.Scatter(x = df['date'], y = df['bike_rides_daily'], name = 'Daily bike rides', marker={'color': df['bike_rides_daily'], 'color': 'darkblue'}), secondary_y = False
)

    fig_2.add_trace(
    go.Scatter(x = df['date'], y = df['avgTemp'], name = 'Daily temperature', marker={'color': df['avgTemp'], 'color': 'lightblue'}), secondary_y = True
)

    fig_2.update_layout(
        title = 'Top 20 most popular bike stations in New York', 
        xaxis_title = 'Start stations',
        yaxis_title = 'Sum of trips',
        height = 400
)
    
    st.plotly_chart(fig_2, use_container_width=True)
    st.markdown("There is an obvious correlation between the rise and drop of temperatures and their relationship with the frequency of bike trips taken daily. As temperatures plunge, so does bike usage. This insight indicates that the shortage problem may be prevalent merely in the warmer months, approximately from May to October.")

    
### BAR CHART PAGE: MOST POPULAR STATIONS

elif page == 'Most popular stations':
    
    # Create the season variable & filter on the side bar
    with st.sidebar:
        season_filter = st.multiselect(label= 'Select the season', options=df['season'].unique(),
    default=df['season'].unique())

    df1 = df.query('season == @season_filter')
    
    # Define the total rides
    total_rides = float(df1['bike_rides_daily'].count())    
    st.metric(label = 'Total Bike Rides', value= numerize(total_rides))

    # Bar chart 
    fig = go.Figure(go.Bar(x = top20['start_station_name'], y = top20['value'], marker = {'color' : top20['value'], 'colorscale' : 'Blues'}))
    fig.update_layout(
        title = 'Top 20 Most Popular Bike Stations in New York',
        xaxis_title = 'Start Stations', 
        yaxis_title = 'Sum of Trips', 
        width = 900, height = 600
)
    
    st.plotly_chart(fig, use_container_width = True)
    st.markdown("From the bar chart it is clear that there are some start stations that are more popular than others - in the top 3 are 6 Ave/W 33 St, West St/Chambers St, and Broadway/W 58 St. There is a significant jump between the highest and lowest bars of the plot, indicating some clear preferences for the leading stations. This is a finding that we could cross reference with the interactive map with aggregated bike trips.")


### MAP PAGE: INTERACTIVE MAP WITH AGGREGATED BIKE TRIPS

elif page == 'Interactive map with aggregated bike trips': 

    # Create the map
    st.write("Interactive map showing aggregated bike trips over New York City")
    
    path_to_html = "CitiBike Trips Aggregated.html"

    # Read file and keep in variable 
    with open(path_to_html, 'r') as f:
        html_data = f.read()

    # Show in webpage
    st.header("Aggregated Bike Trips in New York City")
    st.components.v1.html(html_data,height=800)
    st.markdown("#### Using the filter on the left hand side of the map we can check whether the most popular start stations also appear in the most popular trips.")
    st.markdown("The most popular start stations are:")
    st.markdown("West St/Chambers St, Broadway/W 58 St and 6 Ave/W 33 St. While having the aggregated bike trips filter enabled, it is apparent that even though 6 Ave/W 33 St is a popular start station, it doesn't account for the most commonly taken trips.")
    st.markdown("Some of the most common routes are between 12 Ave/W 40 St, 10 Ave/W 14 St, and West St/Chambers St, which are located along the water, or routes located around the perimeter of Central Park.")


### HISTOGRAMS: CLASSIC VERSUS ELECTRIC BIKES

elif page == "Classic versus electric bikes":

    # Filter DataFrame by category
    classic_bike = df_hist[df_hist["rideable_type"] == "classic_bike"]
    electric_bike = df_hist[df_hist["rideable_type"] == "electric_bike"]

    # Create histograms for each category
    hist_data_A = go.Histogram(x = classic_bike['avgTemp'], name = 'Classic Bike', marker = dict(color = 'darkblue'))
    hist_data_B = go.Histogram(x = electric_bike['avgTemp'], name = 'Electric Bike', marker = dict(color = 'lightblue'))

    # Create layout
    layout = go.Layout(
        title = 'Classic vs Electric Bike Rentals by Temperature',
        xaxis = dict(title = 'Average Temperature'),
        yaxis = dict(title = 'Frequency'),
        barmode = 'overlay'
    )

    # Create the figure
    fig3 = go.Figure(data = [hist_data_A, hist_data_B], layout = layout)

    # Display the figure
    st.plotly_chart(fig3)

    st.markdown('The data shows that classic bikes are rented more often when the temperature is warmer. Electric bikes are rented slightly more often when the temperature is warmer, however relative to classic bikes, electric bike rentals do not change much with the temperature.')
    st.markdown('Additionally, the data shows that classic bikes are rented over 2.5 times more often than electric bikes. This limited electric bike availability helps to explain why their rental does not change much with the weather, as they may simply not be an option most of the time.')
    
    
### CONCLUSIONS PAGE: RECOMMENDATIONS

else:
    
    st.header("Conclusions and recommendations")
    bikes = Image.open("bike.jpg")  #source: https://unsplash.com/photos/blue-citi-bike-bicycles-parked-on-sidewalk-8ol9rD0BHAU?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash
    st.image(bikes)
    st.markdown("### Our analysis has shown that Citi Bikes should focus on the following objectives moving forward:")
    st.markdown("- There is a clear popularity among the stations along the water and around Central Park. I recommend adding bikes and bike parking to these locations.")
    st.markdown("- There is a clear correlation between temperature and bike trips. Ensure that bikes are fully stocked in all these stations during the warmer months in order to meet the higher demand, but provide a lower supply in winter and late autumn to reduce logistics costs")
    st.markdown("- Classic bikes are rented over 2.5 times more often than electric bikes due to limited electric bike availability. I recommend incorporating more electric bikes into circulation when new bikes are added.")