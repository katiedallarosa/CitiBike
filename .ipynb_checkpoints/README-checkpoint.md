# Citi Bike Analysis using Python
Acting as the lead analyst for a bike-sharing service based in New York City, USA. My team has been tasked with analyzing user behavior to help the business strategy department assess the current logistics model of bike distribution across the city and identify expansion opportunities.
# Project
![Citi Bike logo](https://github.com/katiedallarosa/CitiBike/blob/main/citi_bike_logo.png)
## Objective
The project’s objective is to conduct a descriptive analysis of existing data and discover actionable insights for the business strategy team to help make informed decisions that will circumvent availability issues and ensure the company’s position as a leader in eco-friendly transportation solutions in the city.
## Context
For this project, I’ll be using public data from New York bike-sharing facilities operated by Citi Bike. For context, Citi Bike’s popularity has increased since its launch in 2013. The company’s marketing strategy promotes bike sharing as a sustainable and convenient means of transportation, which has been very successful. Since the Covid–19 pandemic, New York residents have found even more merit in bike sharing, creating higher demand. This has led to distribution problems—such as fewer bikes at popular bike stations or stations full of docked bikes, making it difficult to return a hired bike—and customer complaints. 

As the lead analyst, my task is to diagnose where distribution issues stem from and advise higher management on a solution based on your diagnosis of the root of the problem—whether it’s sheer numbers, seasonal demand, or something else. Being in a management position also makes me the bridge between divisions, which requires me to ensure the information is tangible for the business development team. To effectively communicate my analysis to non-analysts, I’ll present my insights in an interactive dashboard depicting the metrics I identify as vital for tackling the distribution issues.
## Key Questions
- What are the most popular stations in the city?
- Is there a weather component at play when it comes to bike usage?
- What are the most popular trips between stations?
- What is the difference in usage between classic and electric bikes?
## Data Source
The project leverages open-source datasets from Citi Bike and NOAA. These resources are integral to addressing the outlined business questions.
- [Open source data from the Citi Bike database for the year 2022.](https://s3.amazonaws.com/tripdata/index.html)
- [Weather data using NOAA’s API service.](https://www.noaa.gov/)
## Tools
- **Pandas**: for data analysis
- **Numpy**: for mathematical equations
- **Seaborn**: for data visualizations
- **Matplotlib**: for data visualizations
- **kepler.gl**: for data visualizations
- **Streamlit**: for data visualizations dashboard
## Stakeholders
The insights derived from this analysis will cater to the business strategy department. 
## Folders
- **01 Project Management**: Project brief.
- **02 Data**: Separated into two subfolders Original and Prepared Data. These contain the original data frames and the data frames after they have been cleaned and prepared for analysis respectively. (Data files not uploaded to GitHub due to size.)
- **03 Scripts**: Jupyter notebooks containing coding for analysis.
- **04 Analysis**: Separated into two subfolders Reports and Visualizations. The Reports subfolder contains crosstabs and the Visualizations subfolder contains the visualizations used for developing and explaining insights.
- **05 Sent to Client**: Final report presented in Streamlit.
## Final Deliverable
For a comprehensive view of my findings and recommendations, please refer to the [Final Project Presentation](https://drive.google.com/file/d/1j7qqMRvDaJZ73--50tT2G0-Kn_9CxN6A/view?usp=sharing) and the Citi Bike folder containing all data sets, graphs, and reports. You may also visit the [Streamlit Citi Bike Dashboard](https://citibike-kdallarosa.streamlit.app/) for full interactivity. 

This analysis is not only about uncovering current trends but also about predicting future customer behaviors, thereby enabling Citi Bike to stay ahead in a competitive market.