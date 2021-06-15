import pandas as pd
import numpy as np
import streamlit as st


url ='https://opendata.ecdc.europa.eu/covid19/nationalcasedeath_eueea_daily_ei/csv/data.csv'
column_names=["Date","Day", "Month", "Year", "Cases", "Deaths", "Country", "Country code", "ISO code", "Population", "Continent"]
data01 = pd.read_csv(url, header=0, names=column_names, usecols=[0,3,4,5,6])
st.title('COVID-19: Deaths')
option=st.selectbox("Date to be displayed:", data01["Date"], index=0)
data01.sort_values(by='Deaths', ascending=False, inplace=True)
st.dataframe(data01.loc[data01["Date"]==option])

#url_vaccine_real ='https://opendata.ecdc.europa.eu/covid19/vaccine_tracker/csv/data.csv'
#column_names_vaccine=["YearWeekISO", "FirstDose","FirstDoseRefused", "SecondDose", "UnknownDose", "NumberDosesReceived", "Region", "Population", "ReportingCountry", "TargetGroup", "Vaccine", "Denominator"] 
#data02 = pd.read_csv(url_vaccine_real, header=0, names=column_names_vaccine, usecols=[0,1,2,3,4,5,6,8,9,10])
#st.title('COVID-19: Vaccines')
#option02=st.selectbox("Country to be displayed:", data02["YearWeekISO"])
#data02.sort_values(by='YearWeekISO', ascending=False, inplace=True)
#st.dataframe(data02.loc[data02["YearWeekISO"]==option02])

st.write("Source: European Centre for Disease Prevention and Control in https://www.ecdc.europa.eu/en")
