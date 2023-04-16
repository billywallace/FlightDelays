import numpy as np
import pickle
import streamlit as st
import altair as alt
import pandas as pd

filename = "trained_arima_model.sav"
loaded_model = pickle.load(open(filename, 'rb'))

forecast = []
for i in loaded_model.predict(n_periods = 312):
    forecast.append(i)

df_forecast = pd.DataFrame(data=forecast, columns=['Forecast'])

# create an altair chart for the app to display
c = alt.Chart(forecast, title='').mark_line().encode(
     x='date', y='value', color='parameter')
chart = (
        alt.Chart(
            data=df_forecast,
            title="Forecasted TSA Checkins Over Time",
        )
        .mark_line()
)


# Simple function to just return the forecast c
def tsa_arima_prediction():
    return forecast



def main():
    st.title('TSA Checkin Prediction Web App')

    st.line_chart(tsa_arima_prediction())



if __name__ == '__main__':
    main()
