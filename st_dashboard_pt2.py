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
    st.markdown("##### Citi Bikes, which is a bike-sharing facility in NYC, runs into a situation where customers complain about bikes not being available at certain times. This analysis will look at the potential reasons behind this. We'll be reviewing key insights from the Citi Bike dashboard to provide helpful insights on the expansion problems Citi Bikes currently faces, which is separated into 5 sections:")
    st.markdown("- Most popular stations")
    st.markdown("- Weather component and bike usage")
    st.markdown("- Interactive map with aggregated bike trips")
    st.markdown("- Classic versus electric bikes")
    st.markdown("- Recommendations")
    st.markdown("##### We will be answering the following questions:")
    st.markdown("- How much would we recommend scaling bikes back between November and April?")
    st.markdown("- How can we determine how many more stations to add along the waterfront?")
    st.markdown("- What are some strategies for ensuring bikes are always stocked at popular stations?")
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
        title = 'Temperature vs Rides in New York City', 
        xaxis_title = 'Start stations',
        yaxis_title = 'Sum of trips',
        height = 400
)
    
    st.plotly_chart(fig_2, use_container_width=True)
    st.markdown("This graph from the Citi Bike Strategy Dashboard shows the relationship between daily bike rides and daily temperature fluctuations throughout the year. The data is in relation to the bike stations in New York City from January 2022 to December 2022.")
    st.markdown("Looking at the data from November to April, we observe a significant drop in bike usage compared to the warmer months. As expected, colder weather and potential inclement conditions contribute to a lower demand for bikes.")
    st.markdown("This data underscores the importance of seasonal adjustments in fleet management and bike stocking strategies.")

    
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
        title = 'Top 20 Most Popular Bike Stations in New York City',
        xaxis_title = 'Start Stations', 
        yaxis_title = 'Sum of Trips', 
        width = 900, height = 600
)
    
    st.plotly_chart(fig, use_container_width = True)
    st.markdown("This bar chart highlights the top 20 most popular bike stations in New York City based on total bike rides, which amount to 372.38K in this dataset. The stations are ranked by the number of trips starting at each location.")
    st.markdown("Taking a closer look at the stations situated along the waterfront, we can observe that stations near parks, tourist areas, and walking paths along the water tend to experience higher traffic, particularly during the warmer months.")
    st.markdown("This data is crucial for optimizing bike availability and managing peak-time shortages at the busiest locations.")


### MAP PAGE: INTERACTIVE MAP WITH AGGREGATED BIKE TRIPS

elif page == 'Interactive map with aggregated bike trips': 

    # Create the map
    st.write("Interactive map showing aggregated bike trips over New York City")
    
    path_to_html = "CitiBike Trips Aggregated.html"

    # Read file and keep in variable 
    with open(path_to_html, 'r') as f:
        html_data = f.read()

    # Show in webpage
    st.components.v1.html(html_data,height=800)
    st.markdown("#### Using the filter on the left hand side of the map we can check whether the most popular start stations also appear in the most popular trips.")
    st.markdown("The most popular start stations are West St/Chambers St, Broadway/W 58 St and 6 Ave/W 33 St. While having the aggregated bike trips filter enabled, it is apparent that even though 6 Ave/W 33 St is a popular start station, it doesn't account for the most commonly taken trips.")
    st.markdown("Some of the most common routes are between 12 Ave/W 40 St, 10 Ave/W 14 St, and West St/Chambers St, which are located along the water, or routes located around the perimeter of Central Park.")
    st.markdown("This map reveals critical routes and areas that are essential for bike redistribution and station expansion efforts, helping optimize bike availability in high-demand areas.")



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

    st.markdown('Classic bikes are rented significantly more often when the temperature is warmer, with a clear increase in rentals as temperatures rise. In contrast, electric bike rentals exhibit less variability with temperature, showing a relatively steady usage pattern.')
    st.markdown('Additionally, the data shows that classic bikes are rented over 2.5 times more often than electric bikes. This limited electric bike availability helps to explain why their rental does not change much with the weather, as they may simply not be an option most of the time.')
    
    
### CONCLUSIONS PAGE: RECOMMENDATIONS

else:
    
    st.header("Conclusions and recommendations")
    bikes = Image.open("bike.jpg")  #source: https://unsplash.com/photos/blue-citi-bike-bicycles-parked-on-sidewalk-8ol9rD0BHAU?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash
    st.image(bikes)
    st.markdown("### Our analysis has shown that Citi Bikes should focus on the following objectives moving forward:")
    st.markdown("- During the months of November through April, scale back the number of bikes by around 30-40%s. This is based on the sharp decrease in ridership during colder months and would help optimize operational costs without negatively affecting rider experience in key areas that still see moderate demand.")
    st.markdown("- To determine how many new stations to add, we would use demand forecasting based on current usage trends at nearby stations, population density, and tourist traffic data. Starting with a 10-15% increase in stations at underserved sections of the waterfront would be a reasonable initial step.")
    st.markdown("- Ensuring bikes are stocked at popular stations would involve real-time rebalancing, dynamic stocking schedules based on peak usage times, and possibly offering incentives for riders to return bikes to underutilized stations. Increasing docking capacity at high-demand locations during peak hours could also prevent shortages.")